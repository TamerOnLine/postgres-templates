# db/models/user_item_settings.py

from sqlalchemy import (
    Column, Integer, Text, Boolean, ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship
from db.models.base import Base

class UserItemSettings(Base):
    __tablename__ = 'user_item_settings'
    __table_args__ = (
        UniqueConstraint('user_id', 'item_id'),
    )

    # 🔑 Primary & Foreign Keys
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id', ondelete='CASCADE'), nullable=False)

    # 🖨️ Print Settings
    print_visible     = Column(Boolean, default=True)
    print_font_size   = Column(Text, default='12pt')
    print_line_height = Column(Text, default='1.5')

    # 🔗 Relationships
    user = relationship("User", back_populates="item_settings")
    item = relationship("Item", back_populates="user_settings")
