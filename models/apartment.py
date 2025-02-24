from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ApartmentBase(BaseModel):
    name: str = Field(..., min_length=5)
    price: int = Field(..., gt=0)
    location: str = Field(..., min_length=5)
    max_occupants: int = Field(..., ge=1, le=10)
    user_id: str = Field(...)

class ApartmentCreate(ApartmentBase):
    pass

class ApartmentUpdate(ApartmentBase):
    pass

class ApartmentResponse(ApartmentBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True 