import os
from fastapi import FastAPI
from src.api import users, trips, locations, bookings
from src.middlewares import error_handler

app = FastAPI(
    title="Travel Planner API",
    version=os.getenv("APP_VERSION", "dev")
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
        "app_version": os.getenv("APP_VERSION", "dev")
    }


