from fastapi import FastAPI
from app.api.routes import (
    survey,
    response,
    analytics,
    admin,
    integration
)
from app.api.middleware import auth, audit
from app.core.events import lifespan
from app.services.notification import register_notification_handlers

app = FastAPI(lifespan=lifespan)

# Register middleware
app.middleware("http")(auth.auth_middleware)
app.middleware("http")(audit.audit_middleware)

