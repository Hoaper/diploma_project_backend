from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel, EmailStr, HttpUrl

class BudgetRange(BaseModel):
    min: int
    max: int

class SocialLinks(BaseModel):
    telegram: Optional[str] = None
    instagram: Optional[str] = None
    facebook: Optional[str] = None

class User(BaseModel):
    user_id: str
    name: str
    surname: Optional[str] = None
    email: EmailStr
    gender: Optional[str] = None
    birth_date: Optional[datetime] = None
    phone: Optional[str] = None
    nationality: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    bio: Optional[str] = None
    university: Optional[str] = None
    student_id_number: Optional[str] = None
    roommate_preferences: Optional[str] = None
    language_preferences: Optional[List[str]] = None
    budget_range: Optional[BudgetRange] = None
    avatar_url: Optional[HttpUrl] = None
    id_document_url: Optional[HttpUrl] = None
    document_verified: bool = False
    social_links: Optional[SocialLinks] = None
    created_at: datetime
    last_login: datetime
    is_landlord: bool = False
    is_verified_landlord: bool = False 