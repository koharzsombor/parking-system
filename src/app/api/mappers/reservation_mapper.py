from app.api.schemas.reservation import ReservationResponse
from app.domain.models.reservation import Reservation


class ReservationMapper:
    @staticmethod
    def to_schema(reservation: Reservation) -> ReservationResponse:
        return ReservationResponse(
            id=reservation.id,
            user_id=reservation.user_id,
            spot_id=reservation.spot_id,
            start_time=reservation.start_time,
            end_time=reservation.end_time
        )

    @staticmethod
    def to_domain(reservation: ReservationResponse) -> Reservation:
        return Reservation(
            id=reservation.id,
            user_id=reservation.user_id,
            spot_id=reservation.spot_id,
            start_time=reservation.start_time,
            end_time=reservation.end_time
        )