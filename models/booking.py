from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class BookingStatus(str, Enum):
    WAITING = "waiting"           # Ожидает рассмотрения
    APPROVAL = "put_on_approval"  # Отправлено на одобрение
    ACCEPT = "accept"            # Принято
    REJECT = "reject"            # Отклонено

class BookingBase(BaseModel):
    apartment_id: str = Field(...)
    user_id: str = Field(...)

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    status: BookingStatus

class BookingResponse(BookingBase):
    id: str
    status: BookingStatus
    created_at: datetime

    class Config:
        orm_mode = True 