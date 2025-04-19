from fastapi import FastAPI
from app.api.routes import (
    survey,
    response,
    analytics,
    admin,
    integration
)
from app.api.middleware.auth import auth_middleware  # Direct import
from app.api.middleware.audit import audit_middleware  # Direct import
from app.core.events import lifespan
from app.services.notification import register_notification_handlers

app = FastAPI(lifespan=lifespan)

# Register middleware
app.middleware("http")(auth_middleware)
app.middleware("http")(audit_middleware)

# Include routers
app.include_router(survey.router, prefix="/surveys", tags=["Surveys"])
app.include_router(response.router, prefix="/responses", tags=["Responses"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
app.include_router(admin.router, prefix="/admin", tags=["Administration"])
app.include_router(integration.router, prefix="/integrate", tags=["Integration"])

# Register event handlers
register_notification_handlers()

def start():
    import uvicorn
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    start()
