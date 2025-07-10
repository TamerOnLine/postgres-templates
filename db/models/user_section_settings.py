from sqlalchemy import Column, Integer, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base



class UserSectionSettings(Base):
    __tablename__ = 'user_section_settings'
    __table_args__ = (
        UniqueConstraint('user_id', 'section_id', name='uix_user_section'),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    section_id = Column(Integer, ForeignKey('sections.id', ondelete='CASCADE'))
    print_visible = Column(Boolean, default=True)
    order_index = Column(Integer)

    user = relationship("User", back_populates="section_settings")
    section = relationship("Section", back_populates="user_settings")
