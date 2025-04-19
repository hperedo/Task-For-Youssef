from app.schemas.notification import NotificationRequest
from app.core.events import event_bus
from typing import Callable

def send_email_notification(patient_email: str, survey_link: str):
    print(f"Sending email to {patient_email} with survey link: {survey_link}")

def register_notification_handlers():
    def handle_survey_notification(data: NotificationRequest):
        if "email" in data.channels:
            send_email_notification(data.patient_id, f"/surveys/{data.survey_id}")
    
    event_bus.subscribe("survey_notification", handle_survey_notification)

