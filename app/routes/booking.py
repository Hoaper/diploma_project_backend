from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.booking import Booking, BookingStatus
from services.booking_service import BookingService
from middleware.auth import TokenData
from dependencies import get_current_user, get_booking_service

router = APIRouter(prefix="/api/v1", tags=["bookings"])

@router.post("/bookings", response_model=Booking)
async def create_booking(
    booking: Booking,
    current_user: TokenData = Depends(get_current_user),
    booking_service: BookingService = Depends(get_booking_service)
):
    booking.user_id = current_user.user_id
    is_available = await booking_service.check_availability(
        booking.apartment_id, booking.check_in_date, booking.check_out_date
    )
    if not is_available:
        raise HTTPException(status_code=400, detail="Apartment not available for these dates")
    return await booking_service.create(booking)

@router.get("/my-bookings", response_model=List[Booking])
async def get_my_bookings(
    current_user: TokenData = Depends(get_current_user),
    booking_service: BookingService = Depends(get_booking_service)
):
    return await booking_service.get_by_user(current_user.user_id)

@router.patch("/bookings/{booking_id}", response_model=Booking)
async def update_booking_status(
    booking_id: str,
    status: BookingStatus,
    current_user: TokenData = Depends(get_current_user),
    booking_service: BookingService = Depends(get_booking_service)
):
    booking = await booking_service.get_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this booking")
    return await booking_service.update_status(booking_id, status) 