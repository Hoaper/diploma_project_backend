from datetime import datetime
from typing import Optional
from pydantic import BaseModel, conint
from enum import Enum

class ReviewType(str, Enum):
    APARTMENT = "apartment"
    USER = "user"

class Review(BaseModel):
    review_id: str
    reviewer_id: str
    target_id: str  # apartment_id or user_id
    review_type: ReviewType
    rating: conint(ge=1, le=5)  # Rating from 1 to 5
    text: str
    created_at: datetime
    updated_at: datetime
    is_verified: bool = False  # For verified stays 