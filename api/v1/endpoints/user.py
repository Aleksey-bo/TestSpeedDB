from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import status, Depends

from schemes.user import UserScheme
from services.user import UserService
from api.v1.dependencies import user_dep


router = APIRouter(prefix="/user", tags=["User"])

user_depends = Annotated[UserService, Depends(user_dep)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(data: UserScheme, user_service: user_depends) -> UserScheme:
    user_action = await user_service.create_handler(data=data.model_dump(exclude=["id"]))
    return user_action