from abc import ABC, abstractmethod
from uuid import UUID

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: UUID):
        pass