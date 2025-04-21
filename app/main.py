from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import (
    survey,
    response,
    analytics,
    admin,
    integration,
    auth,
    user
)
from app.api.middleware import auth_middleware, audit_middleware
from app.core.events import lifespan
from app.services.notification import register_notification_handlers
from app.db.base import Base
from app.db.session import engine
Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan=lifespan)

# Add CORS middleware if needed (uncomment and configure as required)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Health System API",
        "docs": {
            "swagger": "http://localhost:8000/docs",
            "redoc": "http://localhost:8000/redoc"
        }
    }

# Register middleware as HTTP middleware
app.middleware("http")(auth_middleware)
app.middleware("http")(audit_middleware)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])
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
