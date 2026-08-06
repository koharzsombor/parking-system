from app.domain.models.parking_spot import ParkingSpot
from app.domain.models.user import User
from app.domain.rules.reservation_eligibility_rule import ReservationEligibilityRule

class HandicapRule(ReservationEligibilityRule):
    """A rule that checks that the handicap permit of the reserver is in line with the spot."""
    def check(self, user: User, spot: ParkingSpot) -> bool:
        if spot.handicapped:
            return user.handicapped

        return True