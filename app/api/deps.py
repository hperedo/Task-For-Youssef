from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import verify_token
from app.schemas.user import UserRole

def get_current_user(token: str = Depends(verify_token)):
    return token  # Returns decoded token payload

def get_current_active_user(current_user: dict = Depends(get_current_user)):
    if not current_user.get("is_active", True):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def require_healthcare_admin(current_user: dict = Depends(get_current_active_user)):
    if current_user.get("role") != UserRole.healthcare_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Healthcare admin privileges required"
        )
    return current_user

def require_medical_staff(current_user: dict = Depends(get_current_active_user)):
    if current_user.get("role") not in [UserRole.healthcare_admin, UserRole.medical_staff]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Medical staff privileges required"
        )
    return current_user

