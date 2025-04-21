# app/schemas/auth.py

from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True  # Pydantic v2

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None  # Include this if your token contains a role

