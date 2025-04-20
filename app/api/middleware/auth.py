from fastapi import Request, HTTPException
from starlette.middleware.base import RequestResponseEndpoint  # Add this import
from app.core.security import verify_token

async def auth_middleware(request: Request, call_next):  # Add call_next
    if request.url.path.startswith(("/redoc", "/docs")):
        if request.headers.get("X-Docs-Auth") != "your-secret-key":
            raise HTTPException(status_code=401)
#        return await call_next(request)  # Pass request to call_next
    
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        token = auth_header.split(" ")[1]
        payload = verify_token(token)
        request.state.user = payload
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    
    return await call_next(request)  # Always return this
