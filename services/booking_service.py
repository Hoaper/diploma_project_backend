from models.booking import BookingCreate, BookingResponse, BookingUpdate, BookingStatus
from repositories.booking_repository import BookingRepository
from fastapi import HTTPException
from datetime import datetime

class BookingService:
    def __init__(self, booking_repository: BookingRepository):
        self.repository = booking_repository

    async def create_booking(self, booking: BookingCreate) -> BookingResponse:
        # Проверяем существующие бронирования
        existing_booking = await self.repository.find_by_user_and_apartment(
            booking.user_id, 
            booking.apartment_id
        )
        
        if existing_booking:
            if existing_booking["status"] == BookingStatus.REJECT:
                raise HTTPException(
                    status_code=400,
                    detail="You cannot book this apartment as your previous booking was rejected"
                )
            elif existing_booking["status"] in [BookingStatus.WAITING, BookingStatus.APPROVAL, BookingStatus.ACCEPT]:
                raise HTTPException(
                    status_code=400,
                    detail="You already have an active booking for this apartment"
                )

        booking_dict = booking.dict()
        booking_dict["created_at"] = datetime.utcnow()
        booking_dict["status"] = BookingStatus.WAITING  # Начальный статус - ожидание

        created_booking = await self.repository.create(booking_dict)
        created_booking["id"] = str(created_booking["_id"])
        return BookingResponse(**created_booking)

    async def update_booking_status(self, booking_id: str, update: BookingUpdate) -> BookingResponse:
        try:
            updated_booking = await self.repository.update(booking_id, update.dict())
            if not updated_booking:
                raise HTTPException(status_code=404, detail="Booking not found")
            
            updated_booking["id"] = str(updated_booking["_id"])
            return BookingResponse(**updated_booking)
        except:
            raise HTTPException(status_code=404, detail="Invalid booking ID")

    async def get_user_bookings(self, user_id: str) -> list[BookingResponse]:
        bookings = await self.repository.find_by_user_id(user_id)
        return [
            BookingResponse(**{**booking, "id": str(booking["_id"])})
            for booking in bookings
        ]

    async def get_apartment_bookings(self, apartment_id: str) -> list[BookingResponse]:
        bookings = await self.repository.find_by_apartment_id(apartment_id)
        return [
            BookingResponse(**{**booking, "id": str(booking["_id"])})
            for booking in bookings
        ]

    async def delete_booking(self, booking_id: str) -> BookingResponse:
        try:
            booking = await self.repository.find_one(booking_id)
            if not booking:
                raise HTTPException(status_code=404, detail="Booking not found")
            
            if booking["status"] == BookingStatus.ACCEPT:
                raise HTTPException(
                    status_code=400,
                    detail="Cannot delete accepted booking"
                )
                
            await self.repository.delete(booking_id)
            booking["id"] = str(booking["_id"])
            return BookingResponse(**booking)
        except:
            raise HTTPException(status_code=404, detail="Invalid booking ID")

    async def get_booking(self, booking_id: str) -> BookingResponse:
        try:
            booking = await self.repository.find_one(booking_id)
            if not booking:
                raise HTTPException(status_code=404, detail="Booking not found")
            booking["id"] = str(booking["_id"])
            return BookingResponse(**booking)
        except:
            raise HTTPException(status_code=404, detail="Invalid booking ID")

    async def get_bookings_by_status(self, status: BookingStatus) -> list[BookingResponse]:
        bookings = await self.repository.find_by_status(status)
        return [
            BookingResponse(**{**booking, "id": str(booking["_id"])})
            for booking in bookings
        ] 