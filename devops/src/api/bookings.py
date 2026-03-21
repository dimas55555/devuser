from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from uuid import UUID
from src.models.booking import Booking
from src.services.booking_service import get_booking_service, BookingService

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=Booking, status_code=status.HTTP_201_CREATED)
def create_booking(booking: Booking, service: BookingService = Depends(get_booking_service)):
    return service.create_booking(booking)

@router.get("/", response_model=List[Booking])
def get_bookings(service: BookingService = Depends(get_booking_service)):
    return service.get_bookings()

@router.get("/{booking_id}", response_model=Booking)
def get_booking(booking_id: UUID, service: BookingService = Depends(get_booking_service)):
    b = service.get_booking(booking_id)
    if not b:
        raise HTTPException(status_code=404, detail="Booking not found")
    return b

@router.get("/user/{user_id}", response_model=List[Booking])
def get_bookings_by_user(user_id: UUID, service: BookingService = Depends(get_booking_service)):
    return service.get_bookings_by_user(user_id)

@router.put("/{booking_id}", response_model=Booking)
def update_booking(booking_id: UUID, updated_booking: Booking, service: BookingService = Depends(get_booking_service)):
    b = service.update_booking(booking_id, updated_booking)
    if not b:
        raise HTTPException(status_code=404, detail="Booking not found")
    return b

@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(booking_id: UUID, service: BookingService = Depends(get_booking_service)):
    deleted = service.delete_booking(booking_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Booking not found")
    return None