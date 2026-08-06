from app.domain.models.user import User
from app.infrastructure.database.models.user_model import UserModel


class UserMapper:
    @staticmethod
    def to_model(user: User) -> UserModel:
        return UserModel(
            id = user.id,
            email = user.email,
            phone = user.phone,
            handicapped = user.handicapped,
            vip = user.vip
        )

    @staticmethod
    def to_domain(user: UserModel) -> User:
        return User(
            id=user.id,
            email=user.email,
            phone=user.phone,
            handicapped=user.handicapped,
            vip=user.vip
        )