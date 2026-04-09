from fastapi import FastAPI
from src.api import users, trips, locations, bookings
from src.middlewares import error_handler

app = FastAPI(title="Travel Planner API")
app.add_middleware(error_handler.ErrorHandlerMiddleware)
error_handler.setup_exception_handlers(app)

app.include_router(users.router)
app.include_router(trips.router)
app.include_router(locations.router)
app.include_router(bookings.router)