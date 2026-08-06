from app.api.schemas.parking_spot import ParkingSpotResponse
from app.domain.models.parking_spot import ParkingSpot


class ParkingSpotMapper:
    """Maps both ways domain parking spots and API schemas"""
    @staticmethod
    def to_schema(parking_spot: ParkingSpot) -> ParkingSpotResponse:
        """Maps a given domain parking spot to an API schema.

        Args:
            parking_spot (ParkingSpot): The domain parking spot.

        Returns:
            A matching API schema.
        """
        return ParkingSpotResponse(
            id=parking_spot.id,
            handicapped=parking_spot.handicapped,
            vip=parking_spot.vip
        )

    @staticmethod
    def to_domain(parking_spot: ParkingSpotResponse) -> ParkingSpot:
        """Maps a given API schema parking spot to a domain class.

        Args:
            parking_spot (ParkingSpotResponse): The API parking spot schema.

        Returns:
            A matching domain class.
        """
        return ParkingSpot(
            id=parking_spot.id,
            handicapped=parking_spot.handicapped,
            vip=parking_spot.vip
        )