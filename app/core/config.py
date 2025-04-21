import os
from pydantic_settings import BaseSettings
from typing import List
from cryptography.fernet import Fernet

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/healthsurveys")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret")
    ENCRYPTION_KEY: str = os.getenv("ENCRYPTION_KEY") or Fernet.generate_key().decode()
    # Add these new settings
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    
    # Validate the encryption key
    @property
    def valid_encryption_key(self):
        try:
            Fernet(self.ENCRYPTION_KEY.encode())
            return self.ENCRYPTION_KEY
        except ValueError:
            new_key = Fernet.generate_key().decode()
            print(f"Invalid ENCRYPTION_KEY, generated new one: {new_key}")
            return new_key

    # Healthcare specific settings
    ALLOWED_DEPARTMENTS: List[str] = ["cardiology", "pediatrics", "oncology"]
    DEFAULT_SURVEY_EXPIRY_DAYS: int = 14
    PHI_FIELDS: List[str] = ["patient_id", "email", "phone_number"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
