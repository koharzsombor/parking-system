from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen=True)
class User:
    """Domain level representation of a reserver.

    Attributes:
        id (UUID): The unique identifier of the reserver.
        email (str): The email address of the reserver.
        phone (str): The phone number of the reserver.
        handicapped (bool): Whether the reserver has a handicapped parking permit.
        vip (bool): Whether the reserver has a VIP status.
    """
    id: UUID
    email: str
    phone: str
    handicapped: bool
    vip: bool