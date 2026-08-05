from app.application.interfaces.spot_repository import SpotRepository
from app.domain.models.parking_spot import ParkingSpot

class QuerySports:
    def __call__(self, spot_repository: SpotRepository) -> list[ParkingSpot]:
        return spot_repository.get_all()
