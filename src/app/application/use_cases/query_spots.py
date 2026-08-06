from app.application.interfaces.spot_repository import SpotRepository
from app.domain.models.parking_spot import ParkingSpot

class QuerySpots:
    def __init__(self, spot_repository: SpotRepository):
        self.spot_repository: SpotRepository = spot_repository

    def __call__(self) -> list[ParkingSpot]:
        return self.spot_repository.get_all()
