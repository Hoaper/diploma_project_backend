from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from models.apartment import Apartment
from services.apartment_service import ApartmentService
from middleware.auth import TokenData
from dependencies import get_current_user, get_apartment_service

router = APIRouter(prefix="/api/v1", tags=["apartments"])

@router.post("/my-apartments", response_model=Apartment)
async def create_apartment(
    apartment: Apartment,
    current_user: TokenData = Depends(get_current_user),
    apartment_service: ApartmentService = Depends(get_apartment_service)
):
    apartment.owner_id = current_user.user_id
    return await apartment_service.create(apartment)

@router.get("/my-apartments", response_model=List[Apartment])
async def get_my_apartments(
    current_user: TokenData = Depends(get_current_user),
    apartment_service: ApartmentService = Depends(get_apartment_service)
):
    return await apartment_service.get_by_owner(current_user.user_id)

@router.get("/apartments/search", response_model=List[Apartment])
async def search_apartments(
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    location: Optional[str] = None,
    university: Optional[str] = None,
    room_type: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    apartment_service: ApartmentService = Depends(get_apartment_service)
):
    return await apartment_service.search(
        min_price, max_price, location, university, room_type, skip, limit
    ) 