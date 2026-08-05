from datetime import datetime
from domain.models.reservation import Reservation
from reservation_availability_rule import ReservationAvailabilityRule

class OverlapRule(ReservationAvailabilityRule):
    def check(self, reservations: list[Reservation], start: datetime, end: datetime) -> bool:
        return any(
            reservation.overlaps(start, end) for reservation in reservations
        )