from typing import List, Optional
from uuid import UUID
from src.models.trip import Trip

class TripService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TripService, cls).__new__(cls)
            cls._instance.trips: List[Trip] = []
        return cls._instance

    def create_trip(self, trip: Trip) -> Trip:
        self.trips.append(trip)
        return trip

    def get_trips(self) -> List[Trip]:
        return self.trips

    def get_trip(self, trip_id: UUID) -> Optional[Trip]:
        return next((t for t in self.trips if t.id == trip_id), None)

    def update_trip(self, trip_id: UUID, updated_trip: Trip) -> Optional[Trip]:
        for idx, t in enumerate(self.trips):
            if t.id == trip_id:
                self.trips[idx] = updated_trip
                return updated_trip
        return None

    def delete_trip(self, trip_id: UUID) -> bool:
        for idx, t in enumerate(self.trips):
            if t.id == trip_id:
                del self.trips[idx]
                return True
        return False

def get_trip_service() -> TripService:
    return TripService()