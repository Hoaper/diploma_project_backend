from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum

class BookingStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class Booking(BaseModel):
    booking_id: str
    apartment_id: str
    user_id: str
    message: Optional[str] = None
    status: BookingStatus = BookingStatus.PENDING
    check_in_date: datetime
    check_out_date: datetime
    created_at: datetime
    updated_at: datetime
    payment_status: str = "pending"  # pending, completed, refunded
    payment_id: Optional[str] = None 