from abc import ABC, abstractmethod
from app.domain.models.parking_spot import ParkingSpot

class SpotRepository(ABC):
    """An interface for a repository for parking spots."""

    @abstractmethod
    def get_by_id(self, spot_id: int) -> ParkingSpot | None:
        """Gets a parking spot from the parking spot ID.

        Args:
            spot_id (int): The ID of the parking spot.

        Returns:
            The parking spot of the given ID.
        """
        pass

    @abstractmethod
    def get_all(self) -> list[ParkingSpot]:
        """Gets a list of all parking spots in the repository.

        Returns:
            A list of all parking spots in the repository.
        """
        pass
