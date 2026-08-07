from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.application.interfaces.reservation_repository import ReservationRepository
from app.domain.models.reservation import Reservation
from app.infrastructure.database.mappers.reservation_mapper import ReservationMapper
from app.infrastructure.database.models.reservation_model import ReservationModel


class SQLReservationRepository(ReservationRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, res_id: UUID) -> Reservation | None:
        model = self.session.scalar(
            select(ReservationModel).where(ReservationModel.id == res_id)
        )

        if model is None:
            return None

        return ReservationMapper.to_domain(model)

    def get_by_user(self, user_id: UUID) -> list[Reservation]:
        models = self.session.scalars(
            select(ReservationModel)
            .where(ReservationModel.user_id == user_id)
        ).all()

        return [ ReservationMapper.to_domain(model) for model in models ]

    def get_by_spot(self, spot_id: int) -> list[Reservation]:
        models = self.session.scalars(
            select(ReservationModel)
            .where(ReservationModel.spot_id == spot_id)
        ).all()

        return [ ReservationMapper.to_domain(model) for model in models ]

    def cancel(self, res_id: UUID) -> None:
        model = self.session.scalar(
            select(ReservationModel).where(ReservationModel.id == res_id)
        )

        if model is None:
            raise ValueError("Model not found!")

        self.session.delete(model)
        self.session.commit()

    def save(self, reservation: Reservation) -> None:
        model = ReservationMapper.to_model(reservation)
        self.session.add(model)
        self.session.commit()