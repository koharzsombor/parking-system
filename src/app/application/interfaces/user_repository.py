from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None:
        """Gets a user from the user ID.

        Args:
            user_id (UUID): The ID of the user.

        Returns:
            The user of the given ID.
        """
        pass