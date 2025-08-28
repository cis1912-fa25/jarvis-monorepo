from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserSignupRequest(BaseModel):
    username: str
    password: str
    first_name: str

class UserSigninRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    first_name: str
    created_at: datetime

    class Config:
        from_attributes = True

class AuthResponse(BaseModel):
    message: str
    user_id: Optional[int] = None

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int