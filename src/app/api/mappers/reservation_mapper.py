from app.api.schemas.reservation import ReservationResponse
from app.domain.models.reservation import Reservation


class ReservationMapper:
    """Maps both ways domain reservations and API schemas"""
    @staticmethod
    def to_schema(reservation: Reservation) -> ReservationResponse:
        """Maps a given domain reservation to an API schema.

        Args:
            reservation (Reservation): The domain reservation.

        Returns:
            A matching API schema.
        """
        return ReservationResponse(
            id=reservation.id,
            user_id=reservation.user_id,
            spot_id=reservation.spot_id,
            start_time=reservation.start_time,
            end_time=reservation.end_time
        )

    @staticmethod
    def to_domain(reservation: ReservationResponse) -> Reservation:
        """Maps a given API schema reservation to a domain class.

        Args:
            reservation (ReservationResponse): The API reservation schema.

        Returns:
            A matching domain class.
        """
        return Reservation(
            id=reservation.id,
            user_id=reservation.user_id,
            spot_id=reservation.spot_id,
            start_time=reservation.start_time,
            end_time=reservation.end_time
        )