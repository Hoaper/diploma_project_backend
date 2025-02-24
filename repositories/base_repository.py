from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

class BaseRepository:
    def __init__(self, database: AsyncIOMotorDatabase, collection_name: str):
        self.database = database
        self.collection = database[collection_name]

    async def find_one(self, id: str):
        return await self.collection.find_one({"_id": ObjectId(id)})

    async def find_all(self):
        cursor = self.collection.find()
        return [doc async for doc in cursor]

    async def create(self, data: dict):
        data["_id"] = ObjectId()
        await self.collection.insert_one(data)
        return data

    async def update(self, id: str, data: dict):
        result = await self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        if result.modified_count:
            return await self.find_one(id)
        return None 