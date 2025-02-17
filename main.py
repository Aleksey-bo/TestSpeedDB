from fastapi import FastAPI
from sqladmin import Admin

from database import engine, Base
from api.routers import routers
from admin.views import views


def get_application() -> FastAPI:

    async def startup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    application = FastAPI()

    application.add_event_handler("startup", startup)

    admin = Admin(application, engine)

    for view in views:
        admin.add_view(view)

    for router in routers:
        application.include_router(router=router, prefix="/api/v1")

    return application


app = get_application()