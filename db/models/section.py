# models/section.py

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base



class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(Text)
    order_index = Column(Integer, default=0)

    # علاقات اختيارية
    user = relationship("User", back_populates="sections", lazy="joined", cascade="all, delete")
