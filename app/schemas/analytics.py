from pydantic import BaseModel
from typing import Dict, Optional

class SurveyAnalytics(BaseModel):
    survey_id: int
    response_count: int
    completion_rate: float
    average_ratings: Optional[Dict[str, float]] = None
    department_stats: Optional[Dict[str, int]] = None

