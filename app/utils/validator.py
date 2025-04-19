from app.core.config import settings

def validate_department(department: str) -> bool:
    return department in settings.ALLOWED_DEPARTMENTS

def validate_phi_fields(data: dict) -> dict:
    """Remove or mask PHI fields"""
    return {
        k: "[REDACTED]" if k in settings.PHI_FIELDS else v
        for k, v in data.items()
    }

