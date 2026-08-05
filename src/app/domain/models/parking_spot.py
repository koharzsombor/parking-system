from dataclasses import dataclass

@dataclass(frozen=True)
class ParkingSpot:
    id: int
    vip: bool
    handicapped: bool