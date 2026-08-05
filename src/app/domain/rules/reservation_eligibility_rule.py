from abc import ABC, abstractmethod
from app.domain.models.user import User
from app.domain.models.parking_spot import ParkingSpot

class ReservationEligibilityRule(ABC):
    @abstractmethod
    def check(self, user: User, spot: ParkingSpot) -> bool:
        pass