from uuid import UUID
from app.application.interfaces.reservation_repository import ReservationRepository


class CancelReservation:
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository: ReservationRepository = reservation_repository

    def __call__(self, reservation_id: UUID):
        self.reservation_repository.cancel(reservation_id)