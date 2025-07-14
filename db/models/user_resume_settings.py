# db/models/user_resume_settings.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

# User Resume Settings Model
class UserResumeSettings(Base):
    __tablename__ = "user_resume_settings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    main_title = Column(String, default="RESUME")

    # 🔗 Relationships
    user = relationship("User", back_populates="resume_settings")
