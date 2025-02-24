from fastapi import APIRouter, Depends
from models.apartment import ApartmentCreate, ApartmentResponse, ApartmentUpdate
from services.apartment_service import ApartmentService
from repositories.apartment_repository import ApartmentRepository
from dependencies.database import get_apartment_repository

router = APIRouter(prefix="/apartments")

def get_apartment_service(
    repository: ApartmentRepository = Depends(get_apartment_repository)
) -> ApartmentService:
    return ApartmentService(repository)

@router.post("/create/", response_model=ApartmentResponse)
async def create_apartment(
    apartment: ApartmentCreate,
    service: ApartmentService = Depends(get_apartment_service)
):
    return await service.create_apartment(apartment)

@router.get("/info/{apartment_id}", response_model=ApartmentResponse)
async def get_apartment(
    apartment_id: str,
    service: ApartmentService = Depends(get_apartment_service)
):
    return await service.get_apartment(apartment_id)

@router.get("/list_all/", response_model=list[ApartmentResponse])
async def get_all_apartments(
    service: ApartmentService = Depends(get_apartment_service)
):
    print("get_all_apartments")
    return await service.get_all_apartments()

@router.put("/update/{apartment_id}", response_model=ApartmentResponse)
async def update_apartment(
    apartment_id: str,
    apartment: ApartmentUpdate,
    service: ApartmentService = Depends(get_apartment_service)
):
    return await service.update_apartment(apartment_id, apartment)

@router.get("/user/{user_id}", response_model=list[ApartmentResponse])
async def get_user_apartments(
    user_id: str,
    service: ApartmentService = Depends(get_apartment_service)
):
    return await service.get_user_apartments(user_id) 