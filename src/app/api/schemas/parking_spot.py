from pydantic import BaseModel

class ParkingSpotResponse(BaseModel):
    id: int
    handicapped: bool
    vip: bool
