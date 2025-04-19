from fastapi import APIRouter, Depends
from app.api.deps import get_db

router = APIRouter()

@router.post("/trigger-survey")
def trigger_survey():
    return {"message": "Survey triggered"}

