from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User:
        pass