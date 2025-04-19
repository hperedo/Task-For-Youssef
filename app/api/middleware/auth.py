from fastapi import Request, HTTPException
from starlette.middleware.base import RequestResponseEndpoint  # Add this import
from app.core.security import verify_token

async def auth_middleware(request: Request, call_next: RequestResponseEndpoint):  # Add call_next
    if request.url.path in ["/docs", "/openapi.json"]:
        return await call_next(request)  # Pass request to call_next
    
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
