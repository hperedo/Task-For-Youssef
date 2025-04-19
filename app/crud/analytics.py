from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.response import SurveyResponse
from app.schemas.analytics import SurveyAnalytics

def get_survey_analytics(db: Session, survey_id: int):
    # Get response count
    response_count = (
        db.query(func.count(SurveyResponse.id))
        .filter(SurveyResponse.survey_id == survey_id)
        .scalar()
    )
    
    # Get completion rate
    completed_count = (
        db.query(func.count(SurveyResponse.id))
        .filter(
            SurveyResponse.survey_id == survey_id,
            SurveyResponse.completed == True
        )
        .scalar()
    )
    
    completion_rate = (completed_count / response_count * 100) if response_count > 0 else 0
    
    return SurveyAnalytics(
        survey_id=survey_id,
        response_count=response_count,
        completion_rate=completion_rate
    )
