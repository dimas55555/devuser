from fastapi import FastAPI
import os

from src.config.settings import settings

from src.db.database import engine
from src.db.base import Base
from src.models.user_orm import UserORM  

from src.api.users import router as users_router
from src.middlewares import error_handler


app = FastAPI(
    title="Travel Planner API (A3)",
    version=os.getenv("APP_VERSION", "dev")
)

app.add_middleware(error_handler.ErrorHandlerMiddleware)
error_handler.setup_exception_handlers(app)


@app.on_event("startup")
def on_startup():
    print(f"Starting application in mode: {settings.TEST_MODE}")

    if settings.TEST_MODE == "db":
        try:
            Base.metadata.create_all(bind=engine)
            print("Tables created successfully!")
        except Exception as e:
            print(f"DB init error: {e}")
    else:
        print("Running in CACHE mode (no DB)")


app.include_router(users_router)


@app.get("/")
def root():
    return {
        "message": "A3 API is running",
        "version": os.getenv("APP_VERSION", "dev"),
        "mode": settings.TEST_MODE
    }


@app.get("/health")
def health():
    return {"status": "ok"}