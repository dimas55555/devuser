from typing import List, Optional
from uuid import UUID, uuid4
from src.models.location import Location

class LocationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LocationService, cls).__new__(cls)
            cls._instance.locations = []
        return cls._instance

    def create_location(self, trip_id: UUID, name: str, country: str) -> Location:
        loc = Location(id=uuid4(), trip_id=trip_id, name=name, country=country)
        self.locations.append(loc)
        return loc

    def get_locations(self) -> List[Location]:
        return self.locations

    def get_trip_locations(self, trip_id: UUID) -> List[Location]:
        return [loc for loc in self.locations if loc.trip_id == trip_id]

    def delete_location(self, location_id: UUID) -> bool:
        for idx, loc in enumerate(self.locations):
            if loc.id == location_id:
                del self.locations[idx]
                return True
        return False

def get_location_service() -> LocationService:
    return LocationService()