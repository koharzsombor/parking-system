from abc import ABC, abstractmethod
from datetime import datetime
from app.domain.models.reservation import Reservation

class ReservationAvailabilityRule(ABC):
    """An interface for rule that check the availability of the parking spot."""
    @abstractmethod
    def check(self, reservations: list[Reservation], start: datetime, end: datetime) -> bool:
        """Checks if the parking spot is available.

        Args:
            reservations (list[Reservation]): The relevant reservations.
            start (datetime): The start of the reservation.
            end (datetime): The end of the reservation.
        """
        pass