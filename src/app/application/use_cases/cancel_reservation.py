from uuid import UUID
from app.application.interfaces.reservation_repository import ReservationRepository


class CancelReservation:
    """A use-case for cancelling reservations.

    Attributes:
            reservation_repository (ReservationRepository): The repository of reservations.
    """
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository: ReservationRepository = reservation_repository

    def __call__(self, reservation_id: UUID):
        """Executes the use-case.

        Args:
            reservation_id (UUID): The ID of the reservation to be cancelled.
        """
        self.reservation_repository.cancel(reservation_id)