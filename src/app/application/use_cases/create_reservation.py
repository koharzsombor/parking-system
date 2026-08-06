from sqlalchemy.sql.functions import user

from app.application.interfaces.reservation_repository import ReservationRepository
from app.domain.models.parking_spot import ParkingSpot
from app.domain.models.reservation import Reservation
from uuid import uuid4, UUID
from datetime import datetime

from app.domain.models.user import User
from app.domain.rules.reservation_availability_rule import ReservationAvailabilityRule
from app.domain.rules.reservation_eligibility_rule import ReservationEligibilityRule


class CreateReservation:
    def __init__(self,
                availability_rules: list[ReservationAvailabilityRule],
                eligibility_rules: list[ReservationEligibilityRule],
                reservation_repository: ReservationRepository):
        self.availability_rules: list[ReservationAvailabilityRule] = availability_rules
        self.eligibility_rules: list[ReservationEligibilityRule] = eligibility_rules
        self.reservation_repository: ReservationRepository = reservation_repository

    def __call__(self,
                reserver: User,
                spot: ParkingSpot,
                start: datetime,
                end: datetime):

        new_reservation : Reservation = Reservation(
            id=uuid4(),
            spot_id=spot.id,
            start_time=start,
            end_time=end,
            user_id=reserver.id
        )

        if all(
            rule.check(self.reservation_repository.get_by_spot(spot.id), start, end) for rule in self.availability_rules
        ) and all(
            rule.check(reserver, spot) for rule in self.eligibility_rules
        ):
            self.reservation_repository.save(new_reservation)
