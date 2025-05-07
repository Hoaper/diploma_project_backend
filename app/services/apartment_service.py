from typing import Optional, List
from datetime import datetime
from models.apartment import Apartment
from repositories.apartment_repository import ApartmentRepository
from services.base import BaseService

class ApartmentService(BaseService[Apartment]):
    def __init__(self, apartment_repository: ApartmentRepository):
        self.apartment_repository = apartment_repository

    async def create(self, apartment: Apartment) -> Apartment:
        apartment.created_at = datetime.utcnow()
        apartment.updated_at = datetime.utcnow()
        return await self.apartment_repository.create(apartment)

    async def get_by_id(self, apartment_id: str) -> Optional[Apartment]:
        return await self.apartment_repository.get_by_id(apartment_id)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Apartment]:
        return await self.apartment_repository.get_all(skip, limit)

    async def update(self, apartment_id: str, apartment: Apartment) -> Optional[Apartment]:
        apartment.updated_at = datetime.utcnow()
        return await self.apartment_repository.update(apartment_id, apartment)

    async def delete(self, apartment_id: str) -> bool:
        return await self.apartment_repository.delete(apartment_id)

    async def get_by_owner(self, owner_id: str) -> List[Apartment]:
        return await self.apartment_repository.get_by_owner(owner_id)

    async def search(
        self,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        location: Optional[str] = None,
        university: Optional[str] = None,
        room_type: Optional[str] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Apartment]:
        return await self.apartment_repository.search(
            min_price, max_price, location, university, room_type, skip, limit
        )

    async def get_nearby(
        self,
        latitude: float,
        longitude: float,
        radius_km: float = 5.0,
        skip: int = 0,
        limit: int = 100
    ) -> List[Apartment]:
        return await self.apartment_repository.get_nearby(
            latitude, longitude, radius_km, skip, limit
        )

    async def get_available(
        self,
        check_in: datetime,
        check_out: datetime,
        skip: int = 0,
        limit: int = 100
    ) -> List[Apartment]:
        return await self.apartment_repository.get_available(
            check_in, check_out, skip, limit
        )

    async def get_promoted(self, skip: int = 0, limit: int = 100) -> List[Apartment]:
        return await self.apartment_repository.get_promoted(skip, limit)

    async def promote_apartment(self, apartment_id: str) -> Optional[Apartment]:
        apartment = await self.apartment_repository.get_by_id(apartment_id)
        if apartment:
            apartment.is_promoted = True
            apartment.updated_at = datetime.utcnow()
            return await self.apartment_repository.update(apartment_id, apartment)
        return None 