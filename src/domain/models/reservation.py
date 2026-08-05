from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass(frozen=True)
class Reservation:
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