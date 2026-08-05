from abc import ABC, abstractmethod
from app.domain.models.parking_spot import ParkingSpot

class SpotRepository(ABC):
    @abstractmethod
    def get_by_id(self, spot_id: int) -> ParkingSpot:
        pass

    @abstractmethod
    def get_all(self) -> list[ParkingSpot]:
        pass
