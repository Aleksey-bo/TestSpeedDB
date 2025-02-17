from typing import Protocol


class UserService(Protocol):
    def __init__(self, user_repository):
        self.user_repository = user_repository()

    async def create_handler(self, data: dict) -> dict:
        try:
            return await self.user_repository.create(data=data)
        except Exception as e:
            raise Exception("Service: Create Error")