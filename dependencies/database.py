from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from fastapi import Request
from repositories.apartment_repository import ApartmentRepository
from repositories.booking_repository import BookingRepository
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
        self.database = self.client[os.getenv("DB_NAME")]

    def get_apartment_repository(self) -> ApartmentRepository:
        return ApartmentRepository(self.database)

    def get_booking_repository(self) -> BookingRepository:
        return BookingRepository(self.database)

    def close(self):
        if self.client:
            self.client.close()

db = Database()

def get_apartment_repository() -> ApartmentRepository:
    return db.get_apartment_repository()

def get_booking_repository() -> BookingRepository:
    return db.get_booking_repository() 