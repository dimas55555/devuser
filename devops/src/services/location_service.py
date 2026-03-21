from typing import List, Optional
from uuid import UUID
from src.models.location import Location

class LocationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LocationService, cls).__new__(cls)
            cls._instance.locations: List[Location] = []
        return cls._instance

    def create_location(self, location: Location) -> Location:
        self.locations.append(location)
        return location

    def get_locations(self) -> List[Location]:
        return self.locations

    def get_location(self, location_id: UUID) -> Optional[Location]:
        return next((l for l in self.locations if l.id == location_id), None)

    def get_locations_by_trip(self, trip_id: UUID) -> List[Location]:
        return [l for l in self.locations if l.trip_id == trip_id]

    def update_location(self, location_id: UUID, updated_location: Location) -> Optional[Location]:
        for idx, l in enumerate(self.locations):
            if l.id == location_id:
                self.locations[idx] = updated_location
                return updated_location
        return None

    def delete_location(self, location_id: UUID) -> bool:
        for idx, l in enumerate(self.locations):
            if l.id == location_id:
                del self.locations[idx]
                return True
        return False

def get_location_service() -> LocationService:
    return LocationService()