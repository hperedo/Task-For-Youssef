# from fastapi import Request, HTTPException
# from starlette.middleware.base import RequestResponseEndpoint  # Add this import
# from app.core.security import verify_token
#
# async def auth_middleware(request: Request, call_next):
#     # Skip auth for root path and docs
#     if request.url.path in ["/", "/redoc", "/docs", "/openapi.json"]:
#         return await call_next(request)
#        return await call_next(request)  # Pass request to call_next
#     
#     auth_header = request.headers.get("Authorization")
#     if not auth_header:
#         raise HTTPException(status_code=401, detail="Not authenticated")
#     
#     try:
#         token = auth_header.split(" ")[1]
#         payload = verify_token(token)
#         request.state.user = payload
#     except Exception as e:
#         raise HTTPException(status_code=401, detail=str(e))
#         
#     if not is_authenticated(request):
#         raise HTTPException(status_code=401, detail="Not authenticated")
#     
#     return await call_next(request)  # Always return this
    
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Public endpoints that don't require authentication
        public_paths = {
            "/",                # Root path
            "/docs",           # Swagger UI
            "/redoc",          # ReDoc
            "/openapi.json",   # OpenAPI schema
            "/favicon.ico"     # Browser favicon request
        }

        # Skip authentication for public paths
        if request.url.path in public_paths:
            return await call_next(request)

        # Your authentication logic here
        try:
            # Example: Check for Authorization header
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                raise HTTPException(status_code=401, detail="Missing authorization header")

            # Verify token or other auth mechanism
            # token = auth_header.split("Bearer ")[-1]
            # if not verify_token(token):
            #     raise HTTPException(status_code=401, detail="Invalid token")

            return await call_next(request)

        except HTTPException as auth_exc:
            return JSONResponse(
                status_code=auth_exc.status_code,
                content={"detail": auth_exc.detail}
            )

# Legacy function-style middleware for backward compatibility
async def auth_middleware(request: Request, call_next):
    middleware = AuthMiddleware(app=None)  # app=None is fine for this usage
    return await middleware.dispatch(request, call_next)
