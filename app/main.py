from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import user, apartment, booking, review

# Initialize FastAPI app
app = FastAPI(title="Student Housing API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router)
app.include_router(apartment.router)
app.include_router(booking.router)
app.include_router(review.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 