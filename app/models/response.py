from sqlalchemy import Column, Integer, ForeignKey, JSON, DateTime, Boolean, String  # Added String import
from sqlalchemy.sql import func
from app.db.base import Base

class SurveyResponse(Base):
    __tablename__ = "survey_responses"
    __table_args__ = {'comment': 'Patient survey responses with PHI'}

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"))
    patient_id = Column(String(50))  # Encrypted
    answers = Column(JSON)
    completed = Column(Boolean, default=False)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())
