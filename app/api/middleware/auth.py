from fastapi import Request, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED
from app.core.security import verify_token

async def auth_middleware(request: Request, call_next):
    # Skip auth for these paths
    excluded_paths = [
        "/",
        "/docs",
        "/openapi.json",
        "/redoc",
        "/auth/token",
        "/auth/login",
        "/users/register"
    ]
    
    if request.url.path in excluded_paths:
        return await call_next(request)
    
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    try:
        scheme, token = auth_header.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme"
            )
        
        payload = verify_token(token)
        request.state.user = payload
    except Exception as e:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    
    response = await call_next(request)
    return response
