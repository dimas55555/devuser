from typing import List, Optional
from uuid import UUID, uuid4
from src.models.trip import Trip

class TripService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TripService, cls).__new__(cls)
            cls._instance.trips = []
        return cls._instance

    def create_trip(self, title: str, user_id: UUID, description: str) -> Trip:
        trip = Trip(id=uuid4(), title=title, user_id=user_id, description=description)
        self.trips.append(trip)
        return trip

    def get_trips(self) -> List[Trip]:
        return self.trips

    def get_trip(self, trip_id: UUID) -> Optional[Trip]:
        return next((trip for trip in self.trips if trip.id == trip_id), None)

    def get_user_trips(self, user_id: UUID) -> List[Trip]:
        return [trip for trip in self.trips if trip.user_id == user_id]

    def update_trip(self, trip_id: UUID, title: str, description: str) -> Optional[Trip]:
        for idx, trip in enumerate(self.trips):
            if trip.id == trip_id:
                self.trips[idx].title = title
                self.trips[idx].description = description
                return self.trips[idx]
        return None

    def delete_trip(self, trip_id: UUID) -> bool:
        for idx, trip in enumerate(self.trips):
            if trip.id == trip_id:
                del self.trips[idx]
                return True
        return False

def get_trip_service() -> TripService:
    return TripService()