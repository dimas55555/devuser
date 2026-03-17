from fastapi import FastAPI

from src.api import users, trips, locations
from src.middlewares import error_handler

app = FastAPI(title="Travel Planner API")

# middleware
app.add_middleware(error_handler.ErrorHandlerMiddleware)

# global exception handler
error_handler.setup_exception_handlers(app)

# routers
app.include_router(users.router)
app.include_router(trips.router)
app.include_router(locations.router)


@app.get("/")
def root():
    return {"message": "Travel Planner API running"}