from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.schemas.user import UserRole

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    full_name = Column(String(100))
    role = Column(Enum(UserRole), default=UserRole.medical_staff)
    is_active = Column(Boolean, default=True)

    # Use string-based relationship to avoid circular imports
    surveys = relationship("Survey", back_populates="creator")
