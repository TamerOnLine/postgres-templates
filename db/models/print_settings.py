# models/print_settings.py

from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey, func
from db.models.base import Base


class PrintSettings(Base):
    __tablename__ = 'print_settings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True)
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
