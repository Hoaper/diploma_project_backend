from datetime import datetime
from typing import Optional
from pydantic import BaseModel, conint
from enum import Enum

class ReviewType(str, Enum):
    APARTMENT = "apartment"
    USER = "user"

class Review(BaseModel):
    reviewId: str
    reviewerId: str
    targetId: str  # apartmentId or userId
    review_type: ReviewType
    rating: conint(ge=1, le=5)  # Rating from 1 to 5
    text: str
    created_at: datetime
    updated_at: datetime
    is_verified: bool = False  # For verified stays 