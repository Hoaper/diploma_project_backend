from typing import Optional, List
from datetime import datetime
from models.booking import Booking, BookingStatus
from repositories.base import BaseRepository

class BookingRepository(BaseRepository[Booking]):
    async def get_by_user(self, user_id: str) -> List[Booking]:
        # Implementation will depend on your database
        pass

    async def get_by_apartment(self, apartment_id: str) -> List[Booking]:
        # Implementation will depend on your database
        pass

    async def get_by_status(
        self,
        status: BookingStatus,
        skip: int = 0,
        limit: int = 100
    ) -> List[Booking]:
        # Implementation will depend on your database
        pass

    async def update_status(
        self,
        booking_id: str,
        status: BookingStatus
    ) -> Optional[Booking]:
        # Implementation will depend on your database
        pass

    async def check_availability(
        self,
        apartment_id: str,
        check_in: datetime,
        check_out: datetime
    ) -> bool:
        # Implementation will depend on your database
        pass 