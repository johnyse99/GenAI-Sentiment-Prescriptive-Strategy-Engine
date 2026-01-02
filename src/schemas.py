from pydantic import BaseModel, Field, validator
from typing import Optional

class ReviewSchema(BaseModel):
    review_id: int
    customer_name: str
    review_text: str = Field(..., min_length=10)
    rating: int = Field(..., ge=1, le=5)

    @validator('review_text')
    def text_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Review text cannot be empty')
        return v