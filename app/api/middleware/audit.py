from fastapi import Request
import json

async def audit_middleware(request: Request, call_next):
    response = await call_next(request)
    
    if request.method in ["POST", "PUT", "DELETE"]:
        audit_log = {
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "user": request.state.user if hasattr(request.state, "user") else None
        }
        print(f"AUDIT LOG: {json.dumps(audit_log)}")
    
    return response
