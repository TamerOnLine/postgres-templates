# db/models/item.py

from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class Item(Base):
    __tablename__ = 'items'

    # 🔑 Primary & Foreign Keys
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id', ondelete='CASCADE'), nullable=False)

    # 📄 Content Fields
    label = Column(Text)
    value = Column(Text)

    # 🖨️ Print Settings
    print_visible = Column(Boolean, default=True)
    print_font_size = Column(Text, default='12pt')
    order_index = Column(Integer, default=0)

    # 🔗 Relationships
    user_settings = relationship(
        "UserItemSettings",
        back_populates="item",
        cascade="all, delete-orphan"
    )
