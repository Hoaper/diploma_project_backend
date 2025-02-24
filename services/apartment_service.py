from models.apartment import ApartmentCreate, ApartmentResponse, ApartmentUpdate
from repositories.apartment_repository import ApartmentRepository
from repositories.booking_repository import BookingRepository
from fastapi import HTTPException
from datetime import datetime

class ApartmentService:
    def __init__(self, apartment_repository: ApartmentRepository, booking_repository: BookingRepository):
        self.repository = apartment_repository
        self.booking_repository = booking_repository

    async def create_apartment(self, apartment: ApartmentCreate) -> ApartmentResponse:
        apartment_dict = apartment.dict()
        apartment_dict["created_at"] = datetime.utcnow()
        
        created_apartment = await self.repository.create(apartment_dict)
        created_apartment["id"] = str(created_apartment["_id"])
        return ApartmentResponse(**created_apartment)

    async def get_apartment(self, apartment_id: str) -> ApartmentResponse:
        try:
            apartment = await self.repository.find_one(apartment_id)
            if not apartment:
                raise HTTPException(status_code=404, detail="Apartment not found")
            apartment["id"] = str(apartment["_id"])
            return ApartmentResponse(**apartment)
        except:
            raise HTTPException(status_code=404, detail="Invalid apartment ID")

    async def get_all_apartments(self) -> list[ApartmentResponse]:
        apartments = await self.repository.find_all()
        return [
            ApartmentResponse(**{**apartment, "id": str(apartment["_id"])})
            for apartment in apartments
        ]

    async def update_apartment(self, apartment_id: str, apartment: ApartmentUpdate) -> ApartmentResponse:
        try:
            apartment_dict = apartment.dict()
            updated_apartment = await self.repository.update(apartment_id, apartment_dict)
            
            if not updated_apartment:
                raise HTTPException(status_code=404, detail="Apartment not found")
                
            updated_apartment["id"] = str(updated_apartment["_id"])
            return ApartmentResponse(**updated_apartment)
        except:
            raise HTTPException(status_code=404, detail="Invalid apartment ID")

    async def get_user_apartments(self, user_id: str) -> list[ApartmentResponse]:
        apartments = await self.repository.find_by_user_id(user_id)
        return [
            ApartmentResponse(**{**apartment, "id": str(apartment["_id"])})
            for apartment in apartments
        ]

    async def check_booking_availability(self, apartment_id: str) -> bool:
        # Проверяем существование апартаментов
        apartment = await self.repository.find_one(apartment_id)
        if not apartment:
            raise HTTPException(status_code=404, detail="Апартаменты не найдены")

        # Получаем все активные бронирования для апартаментов
        active_bookings = await self.booking_repository.find_by_query({
            "apartment_id": apartment_id,
            "status": {"$ne": "reject"}  # Исключаем отклоненные бронирования
        })

        # Проверяем количество активных бронирований
        if len(active_bookings) >= apartment["max_occupants"]:
            return False
        return True 