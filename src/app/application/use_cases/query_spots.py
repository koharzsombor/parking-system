from app.application.interfaces.spot_repository import SpotRepository
from app.domain.models.parking_spot import ParkingSpot

class QuerySpots:
    """A use-case that finds all the parking spots.

    Attributes:
        spot_repository (SpotRepository): The repository of parking spots.
    """
    def __init__(self, spot_repository: SpotRepository):
        self.spot_repository: SpotRepository = spot_repository

    def __call__(self) -> list[ParkingSpot]:
        """Executes the use-case.

        Returns:
            A list of all parking spots.
        """
        return self.spot_repository.get_all()
