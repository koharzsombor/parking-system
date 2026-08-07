from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.application.interfaces.user_repository import UserRepository
from app.domain.models.user import User
from app.infrastructure.database.mappers.user_mapper import UserMapper
from app.infrastructure.database.models.user_model import UserModel


class SQLUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: UUID) -> User | None:
        model = self.session.scalar(
            select(UserModel).where(UserModel.id == user_id)
        )

        if model is None:
            return None

        return UserMapper.to_domain(model)