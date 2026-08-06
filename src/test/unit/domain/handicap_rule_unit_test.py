from uuid import uuid4

from app.domain.models.parking_spot import ParkingSpot
from app.domain.models.user import User
from app.domain.rules.handicap_rule import HandicapRule


def test_handicapped_user_at_not_handicapped():
    #Arrange
    user = User(
        id = uuid4(),
        email="joe.swanson@yahoo.com",
        phone="+36 1 123 4567",
        vip=False,
        handicapped=True
    )
    spot = ParkingSpot(
        id = 0,
        handicapped=False,
        vip=False
    )
    rule = HandicapRule()

    #Act
    allowed = rule.check(user, spot)

    #Assert
    assert allowed

def test_handicapped_user_at_handicapped():
    #Arrange
    user = User(
        id = uuid4(),
        email="joe.swanson@yahoo.com",
        phone="+36 1 123 4567",
        vip=False,
        handicapped=True
    )
    spot = ParkingSpot(
        id = 0,
        handicapped=True,
        vip=False
    )
    rule = HandicapRule()

    #Act
    allowed = rule.check(user, spot)

    #Assert
    assert allowed

def test_not_handicapped_user_at_not_handicapped():
    # Arrange
    user = User(
        id=uuid4(),
        email="peter.griffin@gmail.com",
        phone="+36 1 123 4569",
        vip=False,
        handicapped=False
    )
    spot = ParkingSpot(
        id=0,
        handicapped=False,
        vip=False
    )
    rule = HandicapRule()

    # Act
    allowed = rule.check(user, spot)

    # Assert
    assert allowed

def test_not_handicapped_user_at_handicapped():
    # Arrange
    user = User(
        id=uuid4(),
        email="peter.griffin@gmail.com",
        phone="+36 1 123 4569",
        vip=False,
        handicapped=False
    )
    spot = ParkingSpot(
        id=0,
        handicapped=True,
        vip=False
    )
    rule = HandicapRule()

    # Act
    allowed = rule.check(user, spot)

    # Assert
    assert not allowed