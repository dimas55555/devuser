from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from uuid import UUID
from src.models.trip import Trip
from src.services.trip_service import get_trip_service, TripService

router = APIRouter(prefix="/trips", tags=["Trips"])

@router.post("/", response_model=Trip, status_code=status.HTTP_201_CREATED)
def create_trip(trip: Trip, service: TripService = Depends(get_trip_service)):
    return service.create_trip(trip)

@router.get("/", response_model=List[Trip])
def get_trips(service: TripService = Depends(get_trip_service)):
    return service.get_trips()

@router.get("/{trip_id}", response_model=Trip)
def get_trip(trip_id: UUID, service: TripService = Depends(get_trip_service)):
    trip = service.get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

@router.put("/{trip_id}", response_model=Trip)
def update_trip(trip_id: UUID, updated_trip: Trip, service: TripService = Depends(get_trip_service)):
    trip = service.update_trip(trip_id, updated_trip)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

@router.delete("/{trip_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trip(trip_id: UUID, service: TripService = Depends(get_trip_service)):
    deleted = service.delete_trip(trip_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Trip not found")
    return None