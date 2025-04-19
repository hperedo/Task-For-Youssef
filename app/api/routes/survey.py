from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.api.deps import require_healthcare_admin, get_current_user
from app import schemas
from app import crud

router = APIRouter()

@router.post("/", response_model=schemas.SurveyOut)
def create_survey(
    survey: schemas.SurveyCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_healthcare_admin)
):
    return crud.survey.create_survey(db, survey, current_user["sub"])

@router.get("/", response_model=List[schemas.SurveyOut])
def read_surveys(
    department: str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.survey.get_surveys(db, department=department, skip=skip, limit=limit)

@router.get("/{survey_id}", response_model=schemas.SurveyOut)
def read_survey(survey_id: int, db: Session = Depends(get_db)):
    survey = crud.survey.get_survey(db, survey_id=survey_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey

@router.put("/{survey_id}", response_model=schemas.SurveyOut)
def update_survey(
    survey_id: int,
    survey: schemas.SurveyUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_healthcare_admin)
):
    db_survey = crud.survey.update_survey(db, survey_id=survey_id, survey=survey)
    if not db_survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return db_survey

@router.delete("/{survey_id}")
def delete_survey(
    survey_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_healthcare_admin)
):
    crud.survey.delete_survey(db, survey_id=survey_id)
    return {"message": "Survey deleted"}

