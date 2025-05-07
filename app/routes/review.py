from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.review import Review, ReviewType
from services.review_service import ReviewService
from middleware.auth import TokenData
from dependencies import get_current_user, get_review_service

router = APIRouter(prefix="/api/v1", tags=["reviews"])

@router.post("/reviews", response_model=Review)
async def create_review(
    review: Review,
    current_user: TokenData = Depends(get_current_user),
    review_service: ReviewService = Depends(get_review_service)
):
    review.reviewer_id = current_user.user_id
    return await review_service.create(review)

@router.get("/reviews/{target_id}", response_model=List[Review])
async def get_reviews(
    target_id: str,
    review_type: ReviewType,
    skip: int = 0,
    limit: int = 100,
    review_service: ReviewService = Depends(get_review_service)
):
    return await review_service.get_by_target(target_id, review_type, skip, limit) 