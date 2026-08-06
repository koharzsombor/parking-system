from dataclasses import dataclass

@dataclass(frozen=True)
class ParkingSpot:
    """Domain level representation of a parking spot.

    Attributes:
        id (int): The number of the parking spot.
        vip (bool): Whether the parking spot is designated as VIP.
        handicapped (bool): Whether the parking spot is designated as handicapped parking.
    """
    id: int
    vip: bool
    handicapped: bool