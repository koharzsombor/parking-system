from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from app.api.mappers.parking_spot_mapper import ParkingSpotMapper
from app.api.mappers.reservation_mapper import ReservationMapper
from app.api.schemas.parking_spot import ParkingSpotResponse
from app.api.schemas.reservation import ReservationResponse
from app.application.use_cases.query_spot import QuerySpot
from app.application.use_cases.query_spot_reservations import QuerySpotReservations
from app.application.use_cases.query_spots import QuerySpots
from app.di.use_cases import get_query_spots, get_query_spot_reservations, get_query_spot

router = APIRouter(
    prefix="/parking_spots",
    tags=["parking_spots"]
)

@router.get("/", response_model=list[ParkingSpotResponse])
def query_parking_spots(query_spots: QuerySpots = Depends(get_query_spots)):
    """Gets all the parking spots in the database."""
    spots = query_spots()
    return [ ParkingSpotMapper.to_schema(spot) for spot in spots ]

@router.get("/{spot_id}/reservations", response_model=list[ReservationResponse])
def query_spot_reservations(spot_id: int,
                            query_reservations: QuerySpotReservations = Depends(get_query_spot_reservations)):
    """Gets all the reservations made on the given spot.

    Args:
        spot_id (int): The ID of the given spot.
    """
    reservations = query_reservations(spot_id=spot_id)
    return [ ReservationMapper.to_schema(reservation) for reservation in reservations ]

@router.get("/{spot_id}", response_model=ParkingSpotResponse)
def query_spot(spot_id: int, use_case: QuerySpot = Depends(get_query_spot)):
    """Gets the parking spot of the given ID.

    Args:
        spot_id (int): The ID of the parking spot.
    """

    spot = use_case(spot_id=spot_id)

    if spot is None:
        raise HTTPException(
            status_code=404,
            detail="Parking spot not found."
        )

    return ParkingSpotMapper.to_schema(spot)