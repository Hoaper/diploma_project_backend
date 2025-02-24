from fastapi import APIRouter, Depends, HTTPException
from models.booking import BookingCreate, BookingResponse, BookingUpdate, BookingStatus
from services.booking_service import BookingService
from services.apartment_service import ApartmentService
from repositories.booking_repository import BookingRepository
from repositories.apartment_repository import ApartmentRepository
from dependencies.database import get_booking_repository, get_apartment_repository

router = APIRouter(prefix="/bookings")

def get_booking_service(
    repository: BookingRepository = Depends(get_booking_repository)
) -> BookingService:
    return BookingService(repository)

def get_apartment_service(
    repository: ApartmentRepository = Depends(get_apartment_repository),
    booking_repository: BookingRepository = Depends(get_booking_repository)
) -> ApartmentService:
    return ApartmentService(repository, booking_repository)

@router.post("/create/", response_model=BookingResponse)
async def create_booking(
    booking: BookingCreate,
    apartment_service: ApartmentService = Depends(get_apartment_service),
    booking_service: BookingService = Depends(get_booking_service)
):
    # Проверяем доступность апартаментов
    is_available = await apartment_service.check_booking_availability(booking.apartment_id)
    
    if not is_available:
        raise HTTPException(
            status_code=400,
            detail="Достигнуто максимальное количество бронирований для этих апартаментов"
        )
    
    return await booking_service.create_booking(booking)

@router.put("/{booking_id}/status", response_model=BookingResponse)
async def update_booking_status(
    booking_id: str,
    update: BookingUpdate,
    service: BookingService = Depends(get_booking_service)
):
    return await service.update_booking_status(booking_id, update)

@router.get("/user/{user_id}", response_model=list[BookingResponse])
async def get_user_bookings(
    user_id: str,
    service: BookingService = Depends(get_booking_service)
):
    return await service.get_user_bookings(user_id)

@router.get("/apartment/{apartment_id}", response_model=list[BookingResponse])
async def get_apartment_bookings(
    apartment_id: str,
    service: BookingService = Depends(get_booking_service)
):
    return await service.get_apartment_bookings(apartment_id)

@router.delete("/{booking_id}", response_model=BookingResponse)
async def delete_booking(
    booking_id: str,
    service: BookingService = Depends(get_booking_service)
):
    return await service.delete_booking(booking_id)

@router.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(
    booking_id: str,
    service: BookingService = Depends(get_booking_service)
):
    return await service.get_booking(booking_id)

@router.get("/status/{status}", response_model=list[BookingResponse])
async def get_bookings_by_status(
    status: BookingStatus,
    service: BookingService = Depends(get_booking_service)
):
    return await service.get_bookings_by_status(status) 