from pydantic import BaseModel, EmailStr
from datetime import datetime

#user registration schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

#user login schema
class UserLogin(BaseModel):
    username: str
    password: str

#user profile schema, we dont want api to send password hash back
class UserProfile(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True
