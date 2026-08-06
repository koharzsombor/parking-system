from uuid import UUID
from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from app.api.mappers.reservation_mapper import ReservationMapper
from app.api.schemas.reservation import ReservationResponse, CreateReservationRequest
from app.application.interfaces.reservation_repository import ReservationRepository
from app.application.interfaces.spot_repository import SpotRepository
from app.application.interfaces.user_repository import UserRepository
from app.application.use_cases.cancel_reservation import CancelReservation
from app.application.use_cases.create_reservation import CreateReservation
from app.di.repositories import get_user_repository, get_spot_repository, get_reservation_repository
from app.di.use_cases import get_create_reservation, get_cancel_reservation

router = APIRouter(
    prefix="/reservations",
    tags=["reservations"]
)

@router.post(
    "/",
    response_model=ReservationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_reservation(
        request: CreateReservationRequest,
        use_case: CreateReservation = Depends(get_create_reservation),
):

    use_case(
        reserver_id=request.user_id,
        spot_id=request.spot_id,
        start=request.start_time,
        end=request.end_time
    )

@router.delete("/{reservation_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def cancel_reservation(
        reservation_id: UUID,
        use_case: CancelReservation = Depends(get_cancel_reservation)
):
    use_case(reservation_id=reservation_id)

@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(reservation_id: UUID,
                    reservation_repository: ReservationRepository = Depends(get_reservation_repository)):

    try:
        reservation = reservation_repository.get_by_id(reservation_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Reservation not found"
        )

    return ReservationMapper.to_schema(reservation)


