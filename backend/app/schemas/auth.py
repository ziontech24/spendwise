from pydantic import BaseModel, EmailStr, Field


# Schema for user login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1)


# Schema for returning an access token
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"