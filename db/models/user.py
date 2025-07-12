# db/models/user.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    # 🔑 Primary Fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔗 Relationships
    sections = relationship(
        "Section",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    item_settings = relationship(
        "UserItemSettings",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    section_settings = relationship(
        "UserSectionSettings",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    project_settings = relationship(
        "UserProjectSettings",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    template_print_settings = relationship(
        "UserTemplatePrintSettings",
        back_populates="user",
        cascade="all, delete-orphan",
        overlaps="template_settings"
    )

    template_settings = relationship(
        "UserTemplatePrintSettings",
        back_populates="user",
        cascade="all, delete-orphan",
        overlaps="template_print_settings"
    )
