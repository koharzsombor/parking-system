from app.api.schemas.user import UserResponse
from app.domain.models.user import User


class UserMapper:
    @staticmethod
    def to_schema(user: User) -> UserResponse:
        return UserResponse(
            id=user.id,
            email=user.email,
            phone=user.phone,
            vip=user.vip,
            handicapped=user.handicapped
        )

    @staticmethod
    def to_domain(user: UserResponse) -> User:
        return User(
            id=user.id,
            email=user.email,
            phone=user.phone,
            vip=user.vip,
            handicapped=user.handicapped
        )