from sqlalchemy.orm import Session
from app.models.survey import Survey
from app.schemas.survey import SurveyCreate, SurveyUpdate
from typing import Optional

def create_survey(db: Session, survey: SurveyCreate, user_id: int):
    db_survey = Survey(**survey.dict(), created_by=user_id)
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def get_survey(db: Session, survey_id: int):
    return db.query(Survey).filter(Survey.id == survey_id).first()

def get_surveys(
    db: Session,
    department: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(Survey)
    if department:
        query = query.filter(Survey.department == department)
    return query.offset(skip).limit(limit).all()

def update_survey(db: Session, survey_id: int, survey: SurveyUpdate):
    db_survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if not db_survey:
        return None
    update_data = survey.dict(exclude_unset=True)
    for field in update_data:
        setattr(db_survey, field, update_data[field])
    db.commit()
    db.refresh(db_survey)
    return db_survey

def delete_survey(db: Session, survey_id: int):
    db.query(Survey).filter(Survey.id == survey_id).delete()
    db.commit()

