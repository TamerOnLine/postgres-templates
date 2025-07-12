# db/models/project.py

from sqlalchemy import (
    Column, Integer, Text, TIMESTAMP, ForeignKey, func
)
from sqlalchemy.orm import relationship
from db.models.base import Base

class Project(Base):
    __tablename__ = 'projects'

    # 🔑 Primary & Foreign Key
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id', ondelete='CASCADE'), nullable=False)

    # 📄 Project Details
    title       = Column(Text)
    description = Column(Text)
    company     = Column(Text)
    link        = Column(Text)
    from_date   = Column(Text)
    to_date     = Column(Text)

    # 🖨️ Print Settings
    print_visible     = Column(Integer, default=True)
    print_font_size   = Column(Text, default='12pt')
    print_line_height = Column(Text, default='1.2')
    order_index       = Column(Integer, default=0)

    # 🕒 Metadata
    created_at = Column(TIMESTAMP, server_default=func.now())

    # 🔗 Relationships
    section = relationship(
        "Section",
        back_populates="projects"
    )

    user_settings = relationship(
        "UserProjectSettings",
        back_populates="project",
        cascade="all, delete-orphan"
    )
