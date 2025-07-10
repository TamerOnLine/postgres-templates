# db/models/item.py
from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from db.models.base import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id', ondelete='CASCADE'))
    label = Column(Text)
    value = Column(Text)
    print_visible = Column(Boolean, default=True)
    print_font_size = Column(Text, default='12pt')
    order_index = Column(Integer, default=0)
