from fastapi import APIRouter, Depends
from uuid import UUID
from src.services.location_service import LocationService, get_location_service

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.post("/")
def create_location(trip_id: UUID, name: str, country: str,
                    service: LocationService = Depends(get_location_service)):
    return service.create_location(trip_id, name, country)


@router.get("/")
def get_locations(service: LocationService = Depends(get_location_service)):
    return service.get_locations()


@router.get("/trip/{trip_id}")
def get_trip_locations(trip_id: UUID,
                       service: LocationService = Depends(get_location_service)):
    return service.get_trip_locations(trip_id)


@router.delete("/{location_id}")
def delete_location(location_id: UUID,
                    service: LocationService = Depends(get_location_service)):
    return service.delete_location(location_id)