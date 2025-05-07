from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from services.user_service import UserService
from middleware.auth import TokenData
from dependencies import get_current_user, get_user_service

router = APIRouter(prefix="/api/v1", tags=["users"])

@router.get("/profile", response_model=User)
async def get_profile(
    current_user: TokenData = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):
    user = await user_service.get_by_id(current_user.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/profile", response_model=User)
async def create_profile(
    user: User,
    current_user: TokenData = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):
    user.user_id = current_user.user_id
    return await user_service.create(user)

@router.patch("/profile", response_model=User)
async def update_profile(
    user: User,
    current_user: TokenData = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):
    user.user_id = current_user.user_id
    updated_user = await user_service.update(current_user.user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user 