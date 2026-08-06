from app.infrastructure.database.base import Base
from sqlalchemy import UUID, BOOLEAN, String
from sqlalchemy.testing.schema import mapped_column

class UserModel(Base):
    __tablename__ = "users"

    id = mapped_column(UUID, primary_key = True)
    email = mapped_column(String)
    phone = mapped_column(String)
    handicapped = mapped_column(BOOLEAN)
    vip = mapped_column(BOOLEAN)


