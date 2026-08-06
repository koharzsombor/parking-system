from app.application.interfaces.reservation_repository import ReservationRepository
from app.application.interfaces.spot_repository import SpotRepository
from app.application.interfaces.user_repository import UserRepository
from app.domain.models.parking_spot import ParkingSpot
from app.domain.models.reservation import Reservation
from uuid import uuid4, UUID
from datetime import datetime
from app.domain.models.user import User
from app.domain.rules.reservation_availability_rule import ReservationAvailabilityRule
from app.domain.rules.reservation_eligibility_rule import ReservationEligibilityRule


class CreateReservation:
    """ A use-case for creating reservations.

        Attributes:
            availability_rules (list[ReservationAvailabilityRule]): Rules for checking parking spot availability.
            eligibility_rules (list[ReservationEligibilityRule]): Rules for checking user eligibility.
            reservation_repository (ReservationRepository): The repository for reservations.
            user_repository (UserRepository): The repository of users.
            spot_repository (SpotRepository): The repository of parking spots.

    """
    def __init__(self,
                availability_rules: list[ReservationAvailabilityRule],
                eligibility_rules: list[ReservationEligibilityRule],
                reservation_repository: ReservationRepository,
                user_repository: UserRepository,
                spot_repository: SpotRepository):
        self.availability_rules: list[ReservationAvailabilityRule] = availability_rules
        self.eligibility_rules: list[ReservationEligibilityRule] = eligibility_rules
        self.reservation_repository: ReservationRepository = reservation_repository
        self.user_repository: UserRepository = user_repository
        self.spot_repository: SpotRepository = spot_repository

    def __call__(self,
                reserver_id: UUID,
                spot_id: int,
                start: datetime,
                end: datetime):
        """Executes the use-case.

            Args:
                reserver_id (UUID): The ID of the reserver.
                spot_id (int): The ID of the parking spot to be reserved.
                start (datetime): The start of the reservation.
                end (datetime): The end of the reservation.
        """

        new_reservation : Reservation = Reservation(
            id=uuid4(),
            spot_id=spot_id,
            start_time=start,
            end_time=end,
            user_id=reserver_id
        )

        reserver = self.user_repository.get_by_id(reserver_id)
        spot = self.spot_repository.get_by_id(spot_id)

        if all(
            rule.check(self.reservation_repository.get_by_spot(spot_id), start, end) for rule in self.availability_rules
        ) and all(
            rule.check(reserver, spot) for rule in self.eligibility_rules
        ):
            self.reservation_repository.save(new_reservation)
