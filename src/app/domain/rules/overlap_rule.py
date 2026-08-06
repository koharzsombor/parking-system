from datetime import datetime
from app.domain.models.reservation import Reservation
from app.domain.rules.reservation_availability_rule import ReservationAvailabilityRule

class OverlapRule(ReservationAvailabilityRule):
    def check(self, reservations: list[Reservation], start: datetime, end: datetime) -> bool:
        return not any(
            reservation.overlaps(start, end) for reservation in reservations
        )