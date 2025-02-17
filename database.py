from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


# engine = create_async_engine('sqlite+aiosqlite:///./freelance.db', echo=True)
engine = create_async_engine('postgresql+asyncpg://postgres:124235768@localhost:5432/freelance', echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()