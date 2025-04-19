from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=schemas.ResponseOut)
def create_response(
    response: schemas.ResponseCreate,
    db: Session = Depends(get_db)
):
    return crud.response.create_response(db, response=response)

@router.get("/{response_id}", response_model=schemas.ResponseOut)
def read_response(response_id: int, db: Session = Depends(get_db)):
    response = crud.response.get_response(db, response_id=response_id)
    if not response:
        raise HTTPException(status_code=404, detail="Response not found")
    return response

@router.get("/survey/{survey_id}", response_model=List[schemas.ResponseOut])
def read_responses_by_survey(
    survey_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.response.get_responses_by_survey(db, survey_id=survey_id, skip=skip, limit=limit)

