from datetime import datetime
from app.domain.models.reservation import Reservation
from uuid import uuid4

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

    #Act
    overlaps = first.overlaps(second.start_time, second.end_time)

    #Assert
    assert overlaps

def test_not_overlapping_before():
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
        start_time=datetime(2026, 8, 5, 8, 0),
        end_time=datetime(2026, 8, 5, 9, 0)
    )

    #Act
    overlaps = first.overlaps(second.start_time, second.end_time)

    #Assert
    assert not overlaps

def test_not_overlapping_after():
    # Arrange
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
        start_time=datetime(2026, 8, 5, 12, 30),
        end_time=datetime(2026, 8, 5, 16, 0)
    )

    # Act
    overlaps = first.overlaps(second.start_time, second.end_time)

    # Assert
    assert not overlaps
