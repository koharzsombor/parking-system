from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass(frozen=True)
class Reservation:
    id: UUID
    user_id: UUID
    spot_id: int
    start_time: datetime
    