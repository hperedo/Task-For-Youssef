from pydantic import BaseModel
from enum import Enum
from typing import List  # Add this import

class NotificationChannel(str, Enum):
    email = "email"
    sms = "sms"
    in_app = "in_app"

class NotificationRequest(BaseModel):
    survey_id: int
    patient_id: str
    channels: List[NotificationChannel]
