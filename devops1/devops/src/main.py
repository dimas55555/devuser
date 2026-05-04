from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.config import get_settings
from src.db.database import engine
from src.db.entities import Base

from src.api import users, trips, locations, bookings
from src.middlewares import error_handler


settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Travel Planner API",
    version=settings.APPLICATION_VERSION,
    lifespan=lifespan
)

app.add_middleware(error_handler.ErrorHandlerMiddleware)
error_handler.setup_exception_handlers(app)

app.include_router(users.router)
app.include_router(trips.router)
app.include_router(locations.router)
app.include_router(bookings.router)


@app.get("/app/info")
def get_app_info():
    return {
        "app_name": "Travel Planner API",
        "app_version": settings.APPLICATION_VERSION
    }