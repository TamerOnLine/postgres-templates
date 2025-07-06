import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import psycopg2

# استيراد كل جدول من مجلد models
from db.create_sections import create_sections_table
from db.create_projects import create_projects_table
from db.create_items import create_items_table
from db.create_print_settings import create_print_settings_table
from db.create_users import create_users_table
from db.create_templates import create_templates_table

# الاتصال بقاعدة البيانات
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)


cur = conn.cursor()

# تنفيذ إنشاء الجداول بالترتيب الصحيح
create_sections_table(cur)
create_projects_table(cur)
create_items_table(cur)
create_print_settings_table(cur)
create_users_table(cur)
create_templates_table(cur)

conn.commit()
cur.close()
conn.close()

print("✅ جميع الجداول أنشئت بنجاح من models/")
