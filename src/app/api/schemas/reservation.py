from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreateReservationRequest(BaseModel):
    """FastAPI Schema for a reservation creation request."""
    user_id: UUID
    spot_id: int
    start_time: datetime
    end_time: datetime


class CancelReservationRequest(BaseModel):
    """FastAPI Schema for a cancellation request (currently not in use)."""
    id: UUID


class ReservationResponse(BaseModel):
    """FastAPI Schema for a Reservation response."""
    id: UUID
    user_id: UUID
    spot_id: int
    start_time: datetime
    end_time: datetime