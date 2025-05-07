from typing import Optional, List
from models.review import Review, ReviewType
from repositories.base import BaseRepository

class ReviewRepository(BaseRepository[Review]):
    async def get_by_target(
        self,
        target_id: str,
        review_type: ReviewType,
        skip: int = 0,
        limit: int = 100
    ) -> List[Review]:
        # Implementation will depend on your database
        pass

    async def get_by_reviewer(
        self,
        reviewer_id: str,
        skip: int = 0,
        limit: int = 100
    ) -> List[Review]:
        # Implementation will depend on your database
        pass

    async def get_average_rating(
        self,
        target_id: str,
        review_type: ReviewType
    ) -> float:
        # Implementation will depend on your database
        pass

    async def verify_review(self, review_id: str) -> Optional[Review]:
        # Implementation will depend on your database
        pass 