from enum import Enum
from typing import Optional  # Add this import
from pydantic import BaseModel

class UserRole(str, Enum):
    healthcare_admin = "healthcare_admin"
    medical_staff = "medical_staff"
    patient = "patient"

class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None  # Now Optional is defined

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.patient

class UserOut(UserBase):
    id: int
    role: UserRole
    is_active: bool
    
    class Config:
        from_attributes = True  # Updated from orm_mode in Pydantic v2
