from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.api.deps import get_db, require_medical_staff

router = APIRouter()

@router.get("/survey/{survey_id}", response_model=schemas.SurveyAnalytics)
def get_survey_analytics(
    survey_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_medical_staff)
):
    return crud.analytics.get_survey_analytics(db, survey_id=survey_id)

