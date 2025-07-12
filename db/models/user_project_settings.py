# db/models/user_project_settings.py

from sqlalchemy import (
    Column, Integer, Boolean, Text, ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship
from db.models.base import Base

class UserProjectSettings(Base):
    __tablename__ = 'user_project_settings'
    __table_args__ = (
        UniqueConstraint('user_id', 'project_id', name='uq_user_project'),
    )

    # 🔑 Primary & Foreign Keys
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id', ondelete='CASCADE'), nullable=False)

    # 🖨️ Print Settings
    print_visible     = Column(Boolean, default=True)
    print_font_size   = Column(Text, default='12pt')
    print_line_height = Column(Text, default='1.5')

    # 🔗 Relationships
    user = relationship("User", back_populates="project_settings")
    project = relationship("Project", back_populates="user_settings")
