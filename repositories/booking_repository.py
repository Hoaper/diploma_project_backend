from .base_repository import BaseRepository
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

class BookingRepository(BaseRepository):
    def __init__(self, database: AsyncIOMotorDatabase):
        super().__init__(database, "bookings")

    async def find_by_user_and_apartment(self, user_id: str, apartment_id: str):
        return await self.collection.find_one({
            "user_id": user_id,
            "apartment_id": apartment_id
        })

    async def find_by_user_id(self, user_id: str):
        cursor = self.collection.find({"user_id": user_id})
        return [doc async for doc in cursor]

    async def find_by_apartment_id(self, apartment_id: str):
        cursor = self.collection.find({"apartment_id": apartment_id})
        return [doc async for doc in cursor]

    async def find_by_status(self, status: str):
        cursor = self.collection.find({"status": status})
        return [doc async for doc in cursor]

    async def delete(self, id: str):
        return await self.collection.delete_one({"_id": ObjectId(id)}) 