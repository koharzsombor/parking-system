from fastapi import Depends
from starlette.middleware.sessions import Session
from .database import get_db
from app.infrastructure.database.repositories.SQL_reservation_repository import SQLReservationRepository
from ..application.interfaces.reservation_repository import ReservationRepository
from ..application.interfaces.spot_repository import SpotRepository
from ..application.interfaces.user_repository import UserRepository
from ..infrastructure.database.repositories.SQL_spot_repository import SQLSpotRepository
from ..infrastructure.database.repositories.SQL_user_repository import SQLUserRepository


def get_reservation_repository(
        session: Session = Depends(get_db)
) -> ReservationRepository:
    return SQLReservationRepository(
        session=session
    )

def get_spot_repository(
        session: Session = Depends(get_db)
) -> SpotRepository:
    return SQLSpotRepository(
        session=session
    )

def get_user_repository(
        session: Session = Depends(get_db)
) -> UserRepository:
    return SQLUserRepository(
        session=session
    )
