from abc import ABC, abstractmethod
from datetime import datetime
from app.domain.models.reservation import Reservation

class ReservationAvailabilityRule(ABC):
    @abstractmethod
    def check(self, reservations: list[Reservation], start: datetime, end: datetime) -> bool:
        pass