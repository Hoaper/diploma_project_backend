from fastapi import Depends
from middleware.auth import TokenData, JWTBearer
from services.user_service import UserService
from services.apartment_service import ApartmentService
from services.booking_service import BookingService
from services.review_service import ReviewService

# JWT middleware
security = JWTBearer()

# Service dependencies
def get_user_service():
    return UserService(None)

def get_apartment_service():
    return ApartmentService(None)

def get_booking_service():
    return BookingService(None)

def get_review_service():
    return ReviewService(None)

# Auth dependency
async def get_current_user(token: TokenData = Depends(security)):
    return token 