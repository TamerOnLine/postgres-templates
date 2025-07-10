# models/user.py

from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from db.models.base import Base  # ✅ احرص أن الاستيراد يتم من base فقط

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

