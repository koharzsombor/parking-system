from uuid import UUID
from abc import ABC, abstractmethod
from domain.models.reservation import Reservation

class ReservationRepository(ABC):
    @abstractmethod
    def save(self, reservation: Reservation) -> None:
        pass

    @abstractmethod
    def get_by_id(self, res_id: UUID) -> Reservation:
        pass

    @abstractmethod
    def get_by_user(self, user_id: UUID) -> list[Reservation]:
        pass

    @abstractmethod
    def get_by_spot(self, spot_id: int) -> list[Reservation]:
        pass