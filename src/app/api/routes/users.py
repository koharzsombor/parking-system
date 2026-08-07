from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from app.api.mappers.user_mapper import UserMapper
from app.api.schemas.user import UserResponse
from app.application.use_cases.query_user import QueryUser
from app.di.use_cases import get_query_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/{user_id}", response_model=UserResponse)
def query_user(user_id: UUID, use_case: QueryUser = Depends(get_query_user)):
    user = use_case(user_id=user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return UserMapper.to_schema(user)