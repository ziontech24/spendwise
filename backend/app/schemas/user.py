from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# Schema for user registration
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)


# Schema for returning user information
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    created_at: datetime