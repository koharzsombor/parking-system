from sqlalchemy import DateTime, UUID, INT
from sqlalchemy.testing.schema import mapped_column
from app.infrastructure.database.base import Base

class ReservationModel(Base):
    __tablename__ = "reservations"

    id = mapped_column(UUID)
    user_id = mapped_column(UUID)
    spot_id = mapped_column(INT)

    start_time = mapped_column(DateTime)
    end_time = mapped_column(DateTime)
