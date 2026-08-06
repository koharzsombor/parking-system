from pydantic import BaseModel
from uuid import UUID


class UserResponse(BaseModel):
    id: UUID
    email: str
    phone: str
    handicapped: bool
    vip: bool