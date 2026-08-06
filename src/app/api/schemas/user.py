from pydantic import BaseModel
from uuid import UUID


class UserResponse(BaseModel):
    """FastAPI Schema for a user response."""
    id: UUID
    email: str
    phone: str
    handicapped: bool
    vip: bool