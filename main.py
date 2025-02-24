from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.apartment import router as apartment_router
from routes.booking import router as booking_router
from dependencies.database import db

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("shutdown")
async def shutdown_db_client():
    db.close()

app.include_router(apartment_router, tags=["apartments"])
app.include_router(booking_router, tags=["bookings"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Apartments API"} 