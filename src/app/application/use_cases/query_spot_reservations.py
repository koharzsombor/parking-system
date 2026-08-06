from app.domain.models.reservation import Reservation
from app.application.interfaces.reservation_repository import ReservationRepository


class QuerySpotReservations:
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository: ReservationRepository = reservation_repository

    def __call__(self, spot_id: int) -> list[Reservation]:
        return self.reservation_repository.get_by_spot(spot_id)