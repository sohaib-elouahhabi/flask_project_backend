from pydantic import BaseModel, Field, validator
from typing import Optional

class CategoryRequestModel(BaseModel):
    name: str = Field(..., max_length=100)  
    description: Optional[str] = Field(None, max_length=200)  

    @validator('name')
    def name_cannot_be_whitespace(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty or just whitespace')
        return v.strip() 

    class Config:
        from_attributes = True
