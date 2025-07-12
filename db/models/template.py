# db/models/template.py

from sqlalchemy import Column, Integer, Text, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base

class Template(Base):
    __tablename__ = "templates"

    # 🔑 Primary Key
    id = Column(Integer, primary_key=True)

    # 📄 Template Details
    name       = Column(Text)
    path       = Column(Text)
    is_default = Column(Boolean, default=False)

    # 🔗 Relationships
    user_settings = relationship(
        "UserTemplatePrintSettings",
        back_populates="template",
        cascade="all, delete-orphan"
    )
