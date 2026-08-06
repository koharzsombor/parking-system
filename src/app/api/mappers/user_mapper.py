from app.api.schemas.user import UserResponse
from app.domain.models.user import User


class UserMapper:
    """Maps both ways domain user classes and API schemas"""

    @staticmethod
    def to_schema(user: User) -> UserResponse:
        """Maps a given domain user class to an API schema.

        Args:
            user (User): The domain user class.

        Returns:
            A matching API schema.
        """
        return UserResponse(
            id=user.id,
            email=user.email,
            phone=user.phone,
            vip=user.vip,
            handicapped=user.handicapped
        )

    @staticmethod
    def to_domain(user: UserResponse) -> User:
        """Maps a given API schema user class to a domain class.

        Args:
            user (UserResponse): The API schema of a user.

        Returns:
            A matching domain class.
        """
        return User(
            id=user.id,
            email=user.email,
            phone=user.phone,
            vip=user.vip,
            handicapped=user.handicapped
        )