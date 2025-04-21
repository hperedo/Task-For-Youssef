from datetime import datetime
from sqlalchemy import Column, Integer, String, JSON, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Survey(Base):
    __tablename__ = "surveys"
    __table_args__ = {'comment': 'Healthcare provider surveys'}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    questions = Column(JSON, nullable=False)
    department = Column(String(100))
    trigger_event = Column(String(50))  # post-visit, post-discharge, etc.
    is_active = Column(Boolean, default=True)
    expiry_days = Column(Integer, default=14)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Use string-based relationship to avoid circular imports
    creator = relationship("User", back_populates="surveys")
