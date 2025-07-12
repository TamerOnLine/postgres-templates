# db/models/user_section_settings.py

from sqlalchemy import (
    Column, Integer, Boolean, ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship
from db.models.base import Base

class UserSectionSettings(Base):
    __tablename__ = 'user_section_settings'
    __table_args__ = (
        UniqueConstraint('user_id', 'section_id', name='uix_user_section'),
    )

    # 🔑 Primary & Foreign Keys
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    section_id = Column(Integer, ForeignKey('sections.id', ondelete='CASCADE'), nullable=False)

    # 🖨️ Section-Specific Settings
    print_visible = Column(Boolean, default=True)
    order_index   = Column(Integer)

    # 🔗 Relationships
    user    = relationship("User", back_populates="section_settings")
    section = relationship("Section", back_populates="user_settings")
