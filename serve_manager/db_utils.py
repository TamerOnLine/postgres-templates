import psycopg2
import os
import sqlite3

from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

DB_PARAMS = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

def get_template_settings(user_id: int, template_id: int):
    try:
        with psycopg2.connect(**DB_PARAMS) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT font_family, font_size, line_height, word_spacing,
                           block_spacing, margin_top, margin_bottom,
                           margin_left, margin_right
                    FROM user_template_print_settings
                    WHERE user_id = %s AND template_id = %s
                """, (user_id, template_id))
                row = cur.fetchone()
        if row:
            return {
                "font_family": row[0],
                "font_size": row[1],
                "line_height": row[2],
                "word_spacing": row[3],
                "block_spacing": row[4],
                "margin_top": row[5],
                "margin_bottom": row[6],
                "margin_left": row[7],
                "margin_right": row[8],
            }
        return {}
    except Exception as e:
        print("❌ Error getting template settings:", e)
        return {}

def get_sections_with_projects(user_id: int):
    try:
        with psycopg2.connect(**DB_PARAMS) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT s.id, s.title,
                           COALESCE(uss.print_visible, true),
                           COALESCE(uss.order_index, s.order_index),
                           p.title, p.description
                    FROM sections s
                    LEFT JOIN user_section_settings uss
                        ON s.id = uss.section_id AND uss.user_id = %s
                    LEFT JOIN projects p
                        ON p.section_id = s.id
                    WHERE s.user_id = %s
                    ORDER BY COALESCE(uss.order_index, s.order_index), p.order_index
                """, (user_id, user_id))
                rows = cur.fetchall()

        sections = {}
        for sid, stitle, visible, s_index, ptitle, pdesc in rows:
            if not visible:
                continue
            if sid not in sections:
                sections[sid] = {"title": stitle, "projects": []}
            if ptitle:
                sections[sid]["projects"].append({
                    "title": ptitle,
                    "description": pdesc
                })

        return list(sections.values())

    except Exception as e:
        print("❌ Error:", e)
        return []




def get_template_path(template_id: int) -> str:
    db_path = os.path.join(os.path.dirname(__file__), "projects.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT path FROM projects WHERE id = ?", (template_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else "two-column-dynamic"

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# إعداد الاتصال من البيئة
DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_pg_session():
    return SessionLocal()

