from app.api.schemas.parking_spot import ParkingSpotResponse
from app.domain.models.parking_spot import ParkingSpot


class ParkingSpotMapper:
    @staticmethod
    def to_schema(parking_spot: ParkingSpot) -> ParkingSpotResponse:
        return ParkingSpotResponse(
            id=parking_spot.id,
            handicapped=parking_spot.handicapped,
            vip=parking_spot.vip
        )

    @staticmethod
    def to_domain(parking_spot: ParkingSpotResponse) -> ParkingSpot:
        return ParkingSpot(
            id=parking_spot.id,
            handicapped=parking_spot.handicapped,
            vip=parking_spot.vip
        )