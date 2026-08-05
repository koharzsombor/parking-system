from app.application.interfaces.reservation_repository import ReservationRepository
from app.domain.models.reservation import Reservation
from uuid import uuid4, UUID
from datetime import datetime


class CreateReservation:
    def __call__(self,
                user_id: UUID,
                spot_id: int,
                reservation_repository: ReservationRepository,
                start: datetime,
                end: datetime):

        new_reservation : Reservation = Reservation(
            id=uuid4(),
            spot_id=spot_id,
            start_time=start,
            end_time=end,
            user_id=user_id
        )

        reservation_repository.save(new_reservation)
