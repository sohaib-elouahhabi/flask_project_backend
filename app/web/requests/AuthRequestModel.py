from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import date
from typing import Optional


class AuthRequestModel(BaseModel):
    """Base model with common validation logic"""
    
    @field_validator('*', mode='before')
    def validate_non_empty(cls, v, info):
        if isinstance(v, str):
            v = v.strip()
            if not v:
                raise ValueError(f'{info.field_name} cannot be empty')
        return v
    
    class Config:
        from_attributes = True


class LoginRequestModel(AuthRequestModel):
    username: str = Field(..., max_length=20)
    password: str = Field(..., max_length=30)


class RegisterRequestModel(AuthRequestModel):
    username: str = Field(..., max_length=20)
    email: EmailStr = Field(...)
    password: str = Field(..., max_length=30, min_length=8)
    confirm_password: str = Field(..., max_length=30)

    
    @field_validator('confirm_password')
    def passwords_match(cls, v: str, info) -> str:
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Passwords do not match')
        return v
    
    @field_validator('password')
    def password_strength(cls, v):
        
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v) or not any(c.islower() for c in v) or not any(c.isdigit() for c in v):
            raise ValueError('Password must contain uppercase, lowercase, and number')
        return v