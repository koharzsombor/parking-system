from fastapi.params import Depends
from app.application.interfaces.reservation_repository import ReservationRepository
from app.application.interfaces.spot_repository import SpotRepository
from app.application.use_cases.cancel_reservation import CancelReservation
from app.application.use_cases.create_reservation import CreateReservation
from app.application.use_cases.query_spot_reservations import QuerySpotReservations
from app.application.use_cases.query_spots import QuerySpots
from app.di.repositories import get_reservation_repository, get_spot_repository
from app.domain.rules.handicap_rule import HandicapRule
from app.domain.rules.overlap_rule import OverlapRule


def get_cancel_reservation(
    reservation_repository: ReservationRepository = Depends(get_reservation_repository)
) -> CancelReservation:
    return CancelReservation(reservation_repository)

def get_create_reservation(
    reservation_repository: ReservationRepository = Depends(get_reservation_repository)
) -> CreateReservation:
    return CreateReservation(
        availability_rules= [ OverlapRule() ],
        eligibility_rules= [ HandicapRule() ],
        reservation_repository= reservation_repository
    )

def get_query_spot_reservations(
        reservation_repository: ReservationRepository = Depends(get_reservation_repository)
) -> QuerySpotReservations:
    return QuerySpotReservations(
        reservation_repository
    )

def get_query_spots(
        spot_repository: SpotRepository = Depends(get_spot_repository)
) -> QuerySpots:
    return QuerySpots(
        spot_repository
    )