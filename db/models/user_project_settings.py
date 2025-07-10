# models/user_project_settings.py

from sqlalchemy import Column, Integer, Boolean, Text, ForeignKey, UniqueConstraint
from db.models.base import Base


class UserProjectSettings(Base):
    __tablename__ = 'user_project_settings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    project_id = Column(Integer, ForeignKey('projects.id', ondelete='CASCADE'))
    print_visible = Column(Boolean, default=True)
    print_font_size = Column(Text, default='12pt')
    print_line_height = Column(Text, default='1.5')

    __table_args__ = (UniqueConstraint('user_id', 'project_id', name='uq_user_project'),)
