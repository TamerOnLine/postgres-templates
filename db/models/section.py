from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
    order_index = Column(Integer)

    # ✅ هذا هو الطرف الآخر من العلاقة
    user = relationship("User", back_populates="sections")
    projects = relationship("Project", back_populates="section", cascade="all, delete-orphan")
    user_settings = relationship("UserSectionSettings", back_populates="section", cascade="all, delete-orphan")

