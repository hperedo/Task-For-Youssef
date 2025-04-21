from enum import Enum
from pydantic import BaseModel
from typing import Optional

class UserRole(str, Enum):
    healthcare_admin = "healthcare_admin"
    medical_staff = "medical_staff"
    patient = "patient"

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None

# Add the missing UserLogin class
class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.patient

class UserOut(UserBase):
    id: int
    role: UserRole
    is_active: bool
    
    class Config:
        from_attributes = True  # Changed from orm_mode
