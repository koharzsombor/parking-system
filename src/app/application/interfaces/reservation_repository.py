from uuid import UUID
from abc import ABC, abstractmethod
from app.domain.models.reservation import Reservation

class ReservationRepository(ABC):
    """An interface for a repository for reservations."""

    @abstractmethod
    def save(self, reservation: Reservation) -> None:
        """Saves the given reservation.

        Args:
            reservation (Reservation): The reservation to be saved.
        """
        pass

    @abstractmethod
    def get_by_id(self, res_id: UUID) -> Reservation | None:
        """Gets a reservation from the reservation ID.

        Args:
            res_id (UUID): The ID of the reservation.

        Returns:
            The reservation of the given ID.
        """
        pass

    @abstractmethod
    def get_by_user(self, user_id: UUID) -> list[Reservation]:
        """Gets all reservations from a given reserver.

        Args:
            user_id (UUID): The ID of the reserver.

        Returns:
            A list of reservations made by the user.
        """
        pass

    @abstractmethod
    def get_by_spot(self, spot_id: int) -> list[Reservation]:
        """Gets all reservations from a given parking spot.

        Args:
            spot_id (UUID): The ID of the parking spot.

        Returns:
            A list of reservations of the parking spot.
        """
        pass

    @abstractmethod
    def cancel(self, res_id: UUID) -> None:
        """Cancels the given reservation.

        Args:
            res_id (UUID): The ID of the reservation to be canceled.
        """
        pass