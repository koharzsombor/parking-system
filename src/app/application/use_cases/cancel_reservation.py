from uuid import UUID
from app.application.interfaces.reservation_repository import ReservationRepository


class CancelReservation:
    def __call__(self,
                reservation_id: UUID,
                reservation_repository: ReservationRepository):
        reservation_repository.cancel(reservation_id)