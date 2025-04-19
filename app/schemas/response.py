from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime

class ResponseBase(BaseModel):
    survey_id: int
    answers: Dict[str, str]
    patient_id: Optional[str] = None

class ResponseCreate(ResponseBase):
    pass

class ResponseOut(ResponseBase):
    id: int
    completed: bool
    submitted_at: datetime
    
    class Config:
        orm_mode = True

