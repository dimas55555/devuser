from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from uuid import UUID
from src.models.location import Location
from src.services.location_service import get_location_service, LocationService

router = APIRouter(prefix="/locations", tags=["Locations"])

@router.post("/", response_model=Location, status_code=status.HTTP_201_CREATED)
def create_location(location: Location, service: LocationService = Depends(get_location_service)):
    return service.create_location(location)

@router.get("/", response_model=List[Location])
def get_locations(service: LocationService = Depends(get_location_service)):
    return service.get_locations()

@router.get("/{location_id}", response_model=Location)
def get_location(location_id: UUID, service: LocationService = Depends(get_location_service)):
    loc = service.get_location(location_id)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc

@router.get("/trip/{trip_id}", response_model=List[Location])
def get_locations_by_trip(trip_id: UUID, service: LocationService = Depends(get_location_service)):
    return service.get_locations_by_trip(trip_id)

@router.put("/{location_id}", response_model=Location)
def update_location(location_id: UUID, updated_location: Location, service: LocationService = Depends(get_location_service)):
    loc = service.update_location(location_id, updated_location)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc

@router.delete("/{location_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_location(location_id: UUID, service: LocationService = Depends(get_location_service)):
    deleted = service.delete_location(location_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Location not found")
    return None