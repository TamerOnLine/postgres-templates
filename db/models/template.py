# models/template.py

from sqlalchemy import Column, Integer, Text, Boolean
from db.models.base import Base


class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    path = Column(Text)
    is_default = Column(Boolean, default=False)
