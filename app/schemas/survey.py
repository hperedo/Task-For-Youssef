from pydantic import BaseModel, Field, validator
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime

class QuestionType(str, Enum):
    text = "text"
    rating = "rating"
    multiple_choice = "multiple-choice"
    likert = "likert"

class QuestionBase(BaseModel):
    id: str = Field(..., min_length=1, max_length=50)
    type: QuestionType
    text: str = Field(..., max_length=250)
    required: bool = True
    options: Optional[List[str]] = None
    
    @validator('options')
    def validate_options(cls, v, values):
        if values.get('type') in ['multiple-choice', 'likert'] and not v:
            raise ValueError("Options required for multiple choice questions")
        return v

class SurveyCreate(BaseModel):
    title: str = Field(..., max_length=200)
    description: Optional[str] = Field(None, max_length=500)
    questions: List[QuestionBase]
    department: Optional[str] = None
    trigger_event: Optional[str] = None
    expiry_days: int = Field(14, ge=1, le=30)

class SurveyUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = None

class SurveyOut(SurveyCreate):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

