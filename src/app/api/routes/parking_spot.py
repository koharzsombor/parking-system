from fastapi import APIRouter
from fastapi.params import Depends

from app.api.mappers.parking_spot_mapper import ParkingSpotMapper
from app.api.mappers.reservation_mapper import ReservationMapper
from app.api.schemas.parking_spot import ParkingSpotResponse
from app.api.schemas.reservation import ReservationResponse
from app.application.use_cases.query_spot_reservations import QuerySpotReservations
from app.application.use_cases.query_spots import QuerySpots
from app.di.use_cases import get_query_spots, get_query_spot_reservations

router = APIRouter(
    prefix="/parking_spots",
    tags=["parking_spots"]
)

@router.get("/", response_model=list[ParkingSpotResponse])
def query_parking_spots(query_spots: QuerySpots = Depends(get_query_spots)):
    """Returns all the parking spots in the database."""
    spots = query_spots()
    return [ ParkingSpotMapper.to_schema(spot) for spot in spots ]

@router.get("/{spot_id}/reservations", response_model=list[ReservationResponse])
def query_spot_reservations(spot_id: int,
                            query_reservations: QuerySpotReservations = Depends(get_query_spot_reservations)):
    """Returns all the reservations made on the given spot.

    Args:
        spot_id (int): The ID of the given spot.
    """
    reservations = query_reservations(spot_id=spot_id)
    return [ ReservationMapper.to_schema(reservation) for reservation in reservations ]
