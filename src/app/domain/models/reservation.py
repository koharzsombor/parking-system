from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass(frozen=True)
class Reservation:
    """Domain level representation of a reservation.

    Attributes:
        id (UUID): Unique identifier of the transaction.
        user_id (UUID): ID of the reserver.
        spot_id (int): ID of the reserved spot.
        start_time (datetime): The time of the beginning of the reservation.
        end_time (datetime): The time of the end of the reservation.
    """
    id: UUID
    user_id: UUID
    spot_id: int
    start_time: datetime
    end_time: datetime

    def overlaps(self, start_time: datetime, end_time: datetime):
        return (
            self.start_time < end_time and
            start_time < self.end_time
        )