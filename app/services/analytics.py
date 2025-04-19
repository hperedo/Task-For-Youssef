from sqlalchemy.orm import Session
from app.crud import analytics as crud_analytics
from app.schemas.analytics import SurveyAnalytics

def generate_analytics_report(db: Session, survey_id: int) -> SurveyAnalytics:
    return crud_analytics.get_survey_analytics(db, survey_id)
    
