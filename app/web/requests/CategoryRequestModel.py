from pydantic import BaseModel, Field, field_validator
from typing import Optional

class CategoryRequestModel(BaseModel):
    name: str = Field(..., max_length=100)  
    description: Optional[str] = Field(None, max_length=200)  

    @field_validator('name')
    def name_cannot_be_whitespace(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be null or empty')
        return v.strip() 

    class Config:
        from_attributes = True
