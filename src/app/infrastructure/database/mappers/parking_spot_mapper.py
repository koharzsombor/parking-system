from app.domain.models.parking_spot import ParkingSpot
from app.infrastructure.database.models.parking_spot_model import ParkingSpotModel

class ParkingSpotMapper:
    @staticmethod
    def to_model(spot: ParkingSpot) -> ParkingSpotModel:
        return ParkingSpotModel(
            id = spot.id,
            vip = spot.vip,
            handicapped = spot.handicapped
        )

    @staticmethod
    def to_domain(spot: ParkingSpotModel) -> ParkingSpot:
        return ParkingSpot(
            id=spot.id,
            vip=spot.vip,
            handicapped=spot.handicapped
        )
