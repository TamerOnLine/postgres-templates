# models/user_template_print_settings.py
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    Text,
    TIMESTAMP,
    ForeignKey,
    UniqueConstraint,
    func
)
from db.models.base import Base


class UserTemplatePrintSettings(Base):
    __tablename__ = 'user_template_print_settings'
    __table_args__ = (
        UniqueConstraint('user_id', 'template_id', name='uq_user_template'),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    template_id = Column(Integer, ForeignKey('templates.id', ondelete='CASCADE'), nullable=False)
    
    font_family = Column(Text, default='Georgia')
    font_size = Column(Text, default='12pt')
    line_height = Column(Text, default='1.5')
    word_spacing = Column(Text, default='3pt')
    block_spacing = Column(Text, default='8px')
    margin_top = Column(Text, default='3cm')
    margin_bottom = Column(Text, default='3cm')
    margin_left = Column(Text, default='3cm')
    margin_right = Column(Text, default='3cm')
    
    created_at = Column(TIMESTAMP, server_default=func.now())

    
    template = relationship("Template", back_populates="user_settings")

    user = relationship(
        "User",
        back_populates="template_settings",
        overlaps="template_print_settings"
    )

