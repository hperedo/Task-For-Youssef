from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from app.core.config import settings

scheduler = BackgroundScheduler()

def schedule_survey(survey_id: int, trigger_time: datetime):
    scheduler.add_job(
        trigger_survey_notification,
        'date',
        run_date=trigger_time,
        args=[survey_id]
    )

def trigger_survey_notification(survey_id: int):
    print(f"Triggering survey {survey_id} notification")

