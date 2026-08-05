from app.infrastructure.database.base import Base
from sqlalchemy import BOOLEAN, INT
from sqlalchemy.testing.schema import mapped_column

class ParkingSpotModel(Base):
    __tablename__ = "parking_spots"

    id = mapped_column(INT)
    vip = mapped_column(BOOLEAN)
    handicapped = mapped_column(BOOLEAN)