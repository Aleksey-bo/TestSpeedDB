from abc import ABC, abstractmethod
from typing import Union, Any
import uuid

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, text

from database import async_session_maker


class AcbstractRepository(ABC):

    @abstractmethod
    async def create(self, data: dict) -> dict:
        pass
    
    @abstractmethod
    async def get(self, id: Union[uuid.UUID, int]) -> dict:
        pass
    
    @abstractmethod
    async def get_all(self, *args: Any, **kwargs: Any) -> list:
        pass
    
    @abstractmethod
    async def update(self, id: Union[uuid.UUID, int], data: dict) -> dict:
        pass
    
    @abstractmethod
    async def delete(self, id: Union[uuid.UUID, int]) -> bool:
        pass


class SqlRepository(AcbstractRepository):
    model = None

    async def create(self, data: dict) -> dict:
        try:
            async with async_session_maker() as session:
                # obj = self.model(**data)
                # session.add(obj)
                # await session.commit()
                # await session.refresh(obj)
                obj = await session.execute(text("INSERT INTO users (name) VALUES(:name) RETURNING id, name"), data)
                await session.commit()
                return obj.fetchone()
                # return obj
        except SQLAlchemyError:
            raise SQLAlchemyError("SQL: Create Error")

    async def get(self, id: Union[uuid.UUID, int]) -> dict:
        try:
            async with async_session_maker() as session:
                obj = select(self.model).filter_by(id)
                res = await session.execute(obj)
                return res.scalar_one()
        except SQLAlchemyError:
            raise SQLAlchemyError("Not Found")

    async def get_all(self, *args: Any, **kwargs: Any) -> list:
        try:
            async with async_session_maker() as session:
                obj = select(self.model).filter_by(**kwargs)
                res = await session.execute(obj)
                return res.scalars()
        except SQLAlchemyError:
            raise SQLAlchemyError("Not Found")

    async def update(self, id: Union[uuid.UUID, int], data: dict) -> dict:
        try:
            async with async_session_maker() as session:
                obj = select(self.model).filter_by(id)

                for key, value in data.items():
                    setattr(obj, key, value)

                await session.commit()
                await session.refresh(obj)
                return obj
        except SQLAlchemyError:
            raise SQLAlchemyError("Not Found")

    async def delete(self, id: Union[uuid.UUID, int]) -> bool:
        try:
            async with async_session_maker() as session:
                obj = select(self.model).filter_by(id)

                await session.delete(obj)
                await session.commit()
                return True
        except SQLAlchemyError:
            raise SQLAlchemyError("Not Found")
            