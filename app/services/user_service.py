from typing import Optional, List
from datetime import datetime
from models.user import User
from repositories.user_repository import UserRepository
from services.base import BaseService

class UserService(BaseService[User]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create(self, user: User) -> User:
        user.created_at = datetime.utcnow()
        user.last_login = datetime.utcnow()
        return await self.user_repository.create(user)

    async def get_by_id(self, user_id: str) -> Optional[User]:
        return await self.user_repository.get_by_id(user_id)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        return await self.user_repository.get_all(skip, limit)

    async def update(self, user_id: str, user: User) -> Optional[User]:
        return await self.user_repository.update(user_id, user)

    async def delete(self, user_id: str) -> bool:
        return await self.user_repository.delete(user_id)

    async def get_by_email(self, email: str) -> Optional[User]:
        return await self.user_repository.get_by_email(email)

    async def update_last_login(self, user_id: str) -> None:
        await self.user_repository.update_last_login(user_id)

    async def verify_landlord(self, user_id: str) -> Optional[User]:
        user = await self.user_repository.get_by_id(user_id)
        if user:
            user.is_landlord = True
            user.is_verified_landlord = True
            return await self.user_repository.update(user_id, user)
        return None

    async def get_landlords(self, skip: int = 0, limit: int = 100) -> List[User]:
        return await self.user_repository.get_landlords(skip, limit)

    async def get_by_university(self, university: str) -> List[User]:
        return await self.user_repository.get_by_university(university) 