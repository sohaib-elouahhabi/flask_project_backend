from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date

class BookRequestModel(BaseModel):
    title: str = Field(...,max_length=100)
    author: str = Field(...,max_length=100)
    published_date: Optional[date] = None
    category_id: int = Field(..., gt=0)

    @field_validator('title', 'author')
    def validate_non_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError('Field cannot be null or empty')
        return value.strip()

    class Config:
        from_attributes = True
