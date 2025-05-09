from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl

class Address(BaseModel):
    street: str
    house_number: str
    apartment_number: str
    entrance: Optional[str] = None
    has_intercom: bool = False
    landmark: Optional[str] = None

class Apartment(BaseModel):
    apartmentId: str
    ownerId: str
    apartment_name: str
    description: str
    address: Address
    district_name: str
    latitude: float
    longitude: float
    price_per_month: int
    area: float
    kitchen_area: float
    floor: int
    number_of_rooms: int
    max_users: int
    available_from: datetime
    available_until: datetime
    university_nearby: str
    pictures: List[HttpUrl]
    is_promoted: bool = False
    is_pet_allowed: bool = False
    rental_type: str  # "room" or "apartment"
    roommate_preferences: Optional[str] = None
    included_utilities: List[str]
    rules: List[str]
    contact_phone: str
    contact_telegram: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    is_active: bool = True 