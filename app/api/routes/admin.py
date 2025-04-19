from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import require_healthcare_admin

router = APIRouter()

@router.get("/users")
def admin_dashboard(current_user: dict = Depends(require_healthcare_admin)):
    return {"message": "Admin dashboard"}

