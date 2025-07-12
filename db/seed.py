
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from sqlalchemy.orm import Session

from db.config import SessionLocal
from db.models import (
    User, Template, UserTemplatePrintSettings,
    Section, Project
)

def seed_database():
    """
    Seed the database with initial data for testing or development.

    This function creates a sample user, a template, print settings,
    a section, and two projects. It uses SQLAlchemy ORM for database
    operations and commits each step to ensure data integrity.
    """
    db: Session = SessionLocal()

    # 1. Create a user
    user = User(name="Tamer", email="tamer@example.com")
    db.add(user)
    db.commit()
    db.refresh(user)

    # 2. Create a resume template
    template = Template(name="Two Column Resume", path="two-column-dynamic", is_default=True)
    db.add(template)
    db.commit()
    db.refresh(template)

    # 3. Set print settings for the user and template
    print_settings = UserTemplatePrintSettings(
        user_id=user.id,
        template_id=template.id,
        font_family="Georgia",
        font_size="14pt",
        line_height="1.5",
        word_spacing="3pt",
        block_spacing="8px",
        margin_top="3cm",
        margin_bottom="3cm",
        margin_left="3cm",
        margin_right="3cm"
    )
    db.add(print_settings)

    # 4. Create a section for projects
    section = Section(user_id=user.id, title="Projects", order_index=1)
    db.add(section)
    db.commit()
    db.refresh(section)

    # 5. Add two project entries to the section
    project1 = Project(
        section_id=section.id,
        title="DeepClone",
        description="Flask tool to extract GitHub folders",
        company="Tamer Dev",
        link="https://github.com/tamer/deepclone",
        from_date="2025-07",
        to_date="2025-08",
        print_visible=True,
        print_font_size="12pt",
        print_line_height="1.4",
        order_index=1
    )

    project2 = Project(
        section_id=section.id,
        title="AI Resume Optimizer",
        description="Python app that tailors resumes using NLP",
        company="OpenAI",
        link="https://github.com/tamer/ai-resume",
        from_date="2023-01",
        to_date="2023-06",
        print_visible=True,
        print_font_size="11pt",
        print_line_height="1.3",
        order_index=2
    )

    db.add_all([project1, project2])
    db.commit()
    db.close()

    print("Database successfully seeded using SQLAlchemy.")


if __name__ == "__main__":
    seed_database()
