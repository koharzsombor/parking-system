from abc import ABC, abstractmethod
from app.domain.models.user import User
from app.domain.models.parking_spot import ParkingSpot

class ReservationEligibilityRule(ABC):
    """An interface for rules that check if a reserver is eligible tp reserve a given parking spot."""
    @abstractmethod
    def check(self, user: User, spot: ParkingSpot) -> bool:
        """Checks if the user is eligible.

        Args:
            user (User): The reserver.
            spot (ParkingSpot): The parking spot.
        Returns:
            Whether the reserver is eligible to reserve the parking spot.
        """
        pass