from pydantic import BaseModel, Field
from typing import Optional

class CategoryRequestModel(BaseModel):
    name: Optional[str] = Field(..., min_length=2, max_length=100)
    
    description: Optional[str] = Field(None, max_length=200)

    class Config:
        orm_mode = True 
