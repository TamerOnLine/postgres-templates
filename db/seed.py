import os
from sqlalchemy.orm import Session
from db.config import SessionLocal
from db.models import (
    User, Template, UserTemplatePrintSettings,
    Section, Project
)

def seed_database():
    db: Session = SessionLocal()

    # ✅ 1. مستخدم
    user = User(name="Tamer", email="tamer@example.com")
    db.add(user)
    db.commit()
    db.refresh(user)

    # ✅ 2. قالب
    template = Template(name="Two Column Resume", path="two-column-dynamic", is_default=True)
    db.add(template)
    db.commit()
    db.refresh(template)

    # ✅ 3. إعدادات طباعة
    db.add(UserTemplatePrintSettings(
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
    ))

    # ✅ 4. قسم
    section = Section(user_id=user.id, title="Projects", order_index=1)
    db.add(section)
    db.commit()
    db.refresh(section)

    # ✅ 5. مشاريع
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
    print("✅ تم تعبئة قاعدة البيانات باستخدام SQLAlchemy!")

if __name__ == "__main__":
    seed_database()
