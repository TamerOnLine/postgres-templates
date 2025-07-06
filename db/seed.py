import os
from dotenv import load_dotenv
load_dotenv()

import psycopg2
from datetime import datetime

# الاتصال بقاعدة البيانات باستخدام متغيرات البيئة
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

# 🧩 1. إدخال قسم تجريبي
cur.execute("""
    INSERT INTO sections (name, print_visible, order_index)
    VALUES (%s, %s, %s)
    RETURNING id;
""", ("Projects", True, 1))
section_id = cur.fetchone()[0]

# 🧩 2. إدخال مشروعين ضمن القسم
projects = [
    (
        section_id,
        "AI Resume Optimizer",
        "A Python-based tool that uses NLP to tailor resumes to job descriptions.",
        "OpenAI",
        "https://github.com/tamer/ai-resume",
        "2023-01",
        "2023-06",
        True,
        "12pt",
        "1.4",
        1
    ),
    (
        section_id,
        "PostgreSQL Dashboard",
        "A Flask web app to manage and visualize PostgreSQL data.",
        "Tamer Tech",
        "https://github.com/tamer/pg-dashboard",
        "2022-05",
        "2022-12",
        True,
        "11pt",
        "1.3",
        2
    )
]

cur.executemany("""
    INSERT INTO projects (
        section_id, title, description, company, link,
        from_date, to_date, print_visible,
        print_font_size, print_line_height, order_index
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
""", projects)

# 🧩 3. إدخال قسم للمهارات
cur.execute("""
    INSERT INTO sections (name, print_visible, order_index)
    VALUES (%s, %s, %s)
    RETURNING id;
""", ("Skills", True, 2))
skills_section_id = cur.fetchone()[0]

skills = [
    (skills_section_id, "Python", "Expert", True, "11pt", 1),
    (skills_section_id, "PostgreSQL", "Advanced", True, "11pt", 2),
    (skills_section_id, "Flask", "Advanced", True, "11pt", 3)
]

cur.executemany("""
    INSERT INTO items (
        section_id, label, value, print_visible, print_font_size, order_index
    )
    VALUES (%s, %s, %s, %s, %s, %s);
""", skills)

conn.commit()
cur.close()
conn.close()

print("✅ تم إدخال بيانات تجريبية بنجاح.")
