from repositories.user import UserRepository
from services.user import UserService


async def user_dep() -> UserService:
    return UserService(
        user_repository=UserRepository
    )