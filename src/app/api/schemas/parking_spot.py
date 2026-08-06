from pydantic import BaseModel

class ParkingSpotResponse(BaseModel):
    """FastAPI Schema for a ParkingSpot response."""
    id: int
    handicapped: bool
    vip: bool
