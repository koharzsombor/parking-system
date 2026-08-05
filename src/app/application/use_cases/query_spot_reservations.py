from app.domain.models.reservation import Reservation
from app.application.interfaces.reservation_repository import ReservationRepository


class QuerySpotReservations:
    def __call__(self,
                spot_id: int,
                reservation_repository: ReservationRepository) -> list[Reservation]:
        return reservation_repository.get_by_spot(spot_id)