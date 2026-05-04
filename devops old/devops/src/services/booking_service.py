from typing import List, Optional
from uuid import UUID
from src.models.booking import Booking

class BookingService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BookingService, cls).__new__(cls)
            cls._instance.bookings: List[Booking] = []
        return cls._instance

    def create_booking(self, booking: Booking) -> Booking:
        self.bookings.append(booking)
        return booking

    def get_bookings(self) -> List[Booking]:
        return self.bookings

    def get_booking(self, booking_id: UUID) -> Optional[Booking]:
        return next((b for b in self.bookings if b.id == booking_id), None)

    def get_bookings_by_user(self, user_id: UUID) -> List[Booking]:
        return [b for b in self.bookings if b.user_id == user_id]

    def update_booking(self, booking_id: UUID, updated_booking: Booking) -> Optional[Booking]:
        for idx, b in enumerate(self.bookings):
            if b.id == booking_id:
                self.bookings[idx] = updated_booking
                return updated_booking
        return None

    def delete_booking(self, booking_id: UUID) -> bool:
        for idx, b in enumerate(self.bookings):
            if b.id == booking_id:
                del self.bookings[idx]
                return True
        return False

def get_booking_service() -> BookingService:
    return BookingService()