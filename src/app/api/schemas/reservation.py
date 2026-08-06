from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreateReservationRequest(BaseModel):
    spot_id: int
    start_time: datetime
    end_time: datetime


class CancelReservationRequest(BaseModel):
    id: UUID


class ReservationResponse(BaseModel):
    id: UUID
    user_id: UUID
    spot_id: int
    start_time: datetime
    end_time: datetime