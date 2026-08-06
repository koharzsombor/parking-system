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
def query_parking_spots(use_case: QuerySpots = Depends(get_query_spots)):
    spots = use_case()
    return [ ParkingSpotMapper.to_schema(spot) for spot in spots ]

@router.get("/{spot_id}/reservations", response_model=list[ReservationResponse])
def query_spot_reservations(spot_id: int,
                            use_case: QuerySpotReservations = Depends(get_query_spot_reservations)):
    reservations = use_case(spot_id=spot_id)
    return [ ReservationMapper.to_schema(reservation) for reservation in reservations ]
