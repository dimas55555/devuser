from fastapi import APIRouter, Depends
from uuid import UUID
from src.services.trip_service import TripService, get_trip_service

router = APIRouter(prefix="/trips", tags=["Trips"])


@router.post("/")
def create_trip(title: str, user_id: UUID, description: str,
                service: TripService = Depends(get_trip_service)):
    return service.create_trip(title, user_id, description)


@router.get("/")
def get_trips(service: TripService = Depends(get_trip_service)):
    return service.get_trips()


@router.get("/{trip_id}")
def get_trip(trip_id: UUID, service: TripService = Depends(get_trip_service)):
    return service.get_trip(trip_id)


@router.get("/user/{user_id}")
def get_user_trips(user_id: UUID, service: TripService = Depends(get_trip_service)):
    return service.get_user_trips(user_id)