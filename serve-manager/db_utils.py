import psycopg2
import os
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
                    SELECT s.id, s.title, p.title, p.description
                    FROM sections s
                    LEFT JOIN projects p ON p.section_id = s.id
                    WHERE s.user_id = %s
                    ORDER BY s.order_index, p.order_index
                """, (user_id,))
                rows = cur.fetchall()

        sections = {}
        for section_id, section_title, project_title, project_desc in rows:
            if section_id not in sections:
                sections[section_id] = {
                    "title": section_title,
                    "projects": []
                }
            if project_title:
                sections[section_id]["projects"].append({
                    "title": project_title,
                    "description": project_desc
                })

        return list(sections.values())
    except Exception as e:
        print("❌ Error getting sections/projects:", e)
        return []
