from uuid import UUID
from app.application.interfaces.user_repository import UserRepository
from app.domain.models.user import User


class QueryUser:
    """Gets a user by their ID.

    Args:
        user_repository (UserRepository): The repository of Users.
    """
    def __init__(self, user_repository: UserRepository):
        self.user_repository: UserRepository = user_repository

    def __call__(self, user_id: UUID) -> User | None:
        """Executes the use-case.

        Args:
            user_id (UUID): The ID of the User.

        Returns:
            The User matching the ID.
        """
        return self.user_repository.get_by_id(user_id)


