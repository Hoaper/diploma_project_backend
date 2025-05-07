from typing import Optional, List
from datetime import datetime
from models.booking import Booking, BookingStatus
from repositories.booking_repository import BookingRepository
from services.base import BaseService

class BookingService(BaseService[Booking]):
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    async def create(self, booking: Booking) -> Booking:
        booking.created_at = datetime.utcnow()
        booking.updated_at = datetime.utcnow()
        return await self.booking_repository.create(booking)

    async def get_by_id(self, booking_id: str) -> Optional[Booking]:
        return await self.booking_repository.get_by_id(booking_id)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Booking]:
        return await self.booking_repository.get_all(skip, limit)

    async def update(self, booking_id: str, booking: Booking) -> Optional[Booking]:
        booking.updated_at = datetime.utcnow()
        return await self.booking_repository.update(booking_id, booking)

    async def delete(self, booking_id: str) -> bool:
        return await self.booking_repository.delete(booking_id)

    async def get_by_user(self, user_id: str) -> List[Booking]:
        return await self.booking_repository.get_by_user(user_id)

    async def get_by_apartment(self, apartment_id: str) -> List[Booking]:
        return await self.booking_repository.get_by_apartment(apartment_id)

    async def get_by_status(
        self,
        status: BookingStatus,
        skip: int = 0,
        limit: int = 100
    ) -> List[Booking]:
        return await self.booking_repository.get_by_status(status, skip, limit)

    async def update_status(
        self,
        booking_id: str,
        status: BookingStatus
    ) -> Optional[Booking]:
        booking = await self.booking_repository.get_by_id(booking_id)
        if booking:
            booking.status = status
            booking.updated_at = datetime.utcnow()
            return await self.booking_repository.update(booking_id, booking)
        return None

    async def check_availability(
        self,
        apartment_id: str,
        check_in: datetime,
        check_out: datetime
    ) -> bool:
        return await self.booking_repository.check_availability(
            apartment_id, check_in, check_out
        )

    async def cancel_booking(self, booking_id: str) -> Optional[Booking]:
        return await self.update_status(booking_id, BookingStatus.CANCELLED)

    async def complete_booking(self, booking_id: str) -> Optional[Booking]:
        return await self.update_status(booking_id, BookingStatus.COMPLETED) 