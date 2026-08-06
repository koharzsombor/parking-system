from sqlalchemy import select
from sqlalchemy.orm import Session
from app.application.interfaces.spot_repository import SpotRepository
from app.domain.models.parking_spot import ParkingSpot
from app.infrastructure.database.mappers.parking_spot_mapper import ParkingSpotMapper
from app.infrastructure.database.models.parking_spot_model import ParkingSpotModel


class SQLSpotRepository(SpotRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, spot_id: int) -> ParkingSpot:
        model = self.session.scalar(
            select(ParkingSpotModel).where(ParkingSpotModel.id == spot_id)
        )

        return ParkingSpotMapper.to_domain(model)

    def get_all(self) -> list[ParkingSpot]:
        models = self.session.scalars(
            select(ParkingSpotModel).order_by(ParkingSpotModel.id)
        ).all()

        return [ ParkingSpotMapper.to_domain(model) for model in models ]