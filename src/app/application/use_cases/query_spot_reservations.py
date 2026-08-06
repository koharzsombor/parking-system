from app.domain.models.reservation import Reservation
from app.application.interfaces.reservation_repository import ReservationRepository


class QuerySpotReservations:
    """A use case which queries all the reservations of a parking spot.

    Attributes:
        reservation_repository (ReservationRepository): The repository of reservations.
    """

    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository: ReservationRepository = reservation_repository

    def __call__(self, spot_id: int) -> list[Reservation]:
        """Executes the use case.

        Args:
            spot_id (int): ID of the spot.

        Returns:
            The list of reservations of the given spot.
        """
        return self.reservation_repository.get_by_spot(spot_id)