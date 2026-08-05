from domain.models.parking_spot import ParkingSpot
from domain.models.user import User
from reservation_eligibility_rule import ReservationEligibilityRule

class HandicapRule(ReservationEligibilityRule):
    def check(self, user: User, spot: ParkingSpot) -> bool:
        if spot.handicapped:
            return user.handicapped

        return True