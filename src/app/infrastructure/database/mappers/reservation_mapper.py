from app.domain.models.reservation import Reservation
from app.infrastructure.database.models.reservation_model import ReservationModel


class ReservationMapper:
    @staticmethod
    def to_model(reservation: Reservation) -> ReservationModel:
        return ReservationModel(
            id = reservation.id,
            user_id = reservation.user_id,
            spot_id = reservation.spot_id,
            start_time = reservation.start_time,
            end_time = reservation.end_time
        )

    @staticmethod
    def to_domain(reservation: ReservationModel) -> Reservation:
        return Reservation(
            id = reservation.id,
            user_id = reservation.user_id,
            spot_id = reservation.spot_id,
            start_time = reservation.start_time,
            end_time = reservation.end_time
        )