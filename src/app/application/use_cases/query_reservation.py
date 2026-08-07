from uuid import UUID
from app.application.interfaces.reservation_repository import ReservationRepository
from app.domain.models.reservation import Reservation


class QueryReservation:
    """Gets a reservation by their ID.

    Args:
        reservation_repository (ReservationRepository): The repository of reservations.
    """
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository: ReservationRepository = reservation_repository

    def __call__(self, reservation_id: UUID) -> Reservation:
        """Executes the use-case.

        Args:
            reservation_id (UUID): The ID of the reservation.

        Returns:
            The reservation matching the ID.
        """
        return self.reservation_repository.get_by_id(reservation_id)


