from sqlalchemy.orm import Session
from app.models.response import SurveyResponse
from app.schemas.response import ResponseCreate
from app.db.encryption import encrypt_data

def create_response(db: Session, response: ResponseCreate):
    # Encrypt PHI fields
    if response.patient_id:
        response.patient_id = encrypt_data(response.patient_id)
    
    db_response = SurveyResponse(**response.dict())
    db.add(db_response)
    db.commit()
    db.refresh(db_response)
    return db_response

def get_response(db: Session, response_id: int):
    return db.query(SurveyResponse).filter(SurveyResponse.id == response_id).first()

def get_responses_by_survey(db: Session, survey_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(SurveyResponse)
        .filter(SurveyResponse.survey_id == survey_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

