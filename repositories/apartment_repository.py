from .base_repository import BaseRepository
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

class ApartmentRepository(BaseRepository):
    def __init__(self, database: AsyncIOMotorDatabase):
        super().__init__(database, "apartments")

    async def find_by_user_id(self, user_id: str):
        cursor = self.collection.find({"user_id": user_id})
        return [doc async for doc in cursor] 