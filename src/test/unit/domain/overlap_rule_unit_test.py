from datetime import datetime
from uuid import uuid4
from app.domain.models.reservation import Reservation
from app.domain.rules.overlap_rule import OverlapRule

def test_overlapping():
    #Arrange
    first = Reservation(
        id=uuid4(),
        user_id=uuid4(),
        spot_id=0,
        start_time=datetime(2026, 8, 5, 10, 0),
        end_time=datetime(2026, 8, 5, 12, 0)
    )
    second = Reservation(
        id=uuid4(),
        user_id=uuid4(),
        spot_id=0,
        start_time=datetime(2026, 8, 5, 11, 0),
        end_time=datetime(2026, 8, 5, 13, 0)
    )

    reservations = [first, second]

    start = datetime(2026, 8, 5, 12, 0)
    end = datetime(2026, 8, 5, 14, 0)

    rule = OverlapRule()

    #Act
    allowed = rule.check(reservations, start, end)

    #Assert
    assert not allowed

def test_not_overlapping():
    #Arrange
    first = Reservation(
        id=uuid4(),
        user_id=uuid4(),
        spot_id=0,
        start_time=datetime(2026, 8, 5, 10, 0),
        end_time=datetime(2026, 8, 5, 12, 0)
    )
    second = Reservation(
        id=uuid4(),
        user_id=uuid4(),
        spot_id=0,
        start_time=datetime(2026, 8, 5, 11, 0),
        end_time=datetime(2026, 8, 5, 13, 0)
    )

    reservations = [first, second]

    start = datetime(2026, 8, 5, 16, 0)
    end = datetime(2026, 8, 5, 18, 0)

    rule = OverlapRule()

    #Act
    allowed = rule.check(reservations, start, end)

    #Assert
    assert allowed