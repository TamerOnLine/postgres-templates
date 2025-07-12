from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey, func
from db.models.base import Base
from sqlalchemy.orm import relationship

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id', ondelete='CASCADE'))
    title = Column(Text)
    description = Column(Text)
    company = Column(Text)
    link = Column(Text)
    from_date = Column(Text)
    to_date = Column(Text)
    print_visible = Column(Integer, default=True)
    print_font_size = Column(Text, default='12pt')
    print_line_height = Column(Text, default='1.2')
    order_index = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now())

    
    section = relationship("Section", back_populates="projects")
    user_settings = relationship("UserProjectSettings", back_populates="project", cascade="all, delete-orphan")

