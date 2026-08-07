from uuid import UUID
from app.application.interfaces.spot_repository import SpotRepository
from app.domain.models.parking_spot import ParkingSpot


class QuerySpot:
    """Gets a parking spot by their ID.

    Args:
        spot_repository (SpotRepository): The repository of parking spots.
    """
    def __init__(self, spot_repository: SpotRepository):
        self.spot_repository: SpotRepository = spot_repository

    def __call__(self, spot_id: int) -> ParkingSpot:
        """Executes the use-case.

        Args:
            spot_id (int): The ID of the parking spot.

        Returns:
            The parking spot matching the ID.
        """
        return self.spot_repository.get_by_id(spot_id)


