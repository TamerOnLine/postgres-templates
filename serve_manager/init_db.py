import os
import json
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "serve-config.json")
DB_PATH = os.path.join(BASE_DIR, "projects.db")

# تحميل إعدادات المشروع
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

# حفظ المسار النسبي كما هو
relative_path = config["relative_path"]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    path TEXT NOT NULL,
    entry TEXT NOT NULL,
    port INTEGER NOT NULL,
    is_running BOOLEAN DEFAULT 0,
    pid INTEGER
)
""")

# إضافة المشروع تلقائيًا (إذا لم يكن موجودًا)
cursor.execute("SELECT COUNT(*) FROM projects WHERE name = ?", (config["name"],))
if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO projects (name, type, path, entry, port)
    VALUES (?, ?, ?, ?, ?)
    """, (
        config["name"],
        config["type"],
        relative_path,  # المسار النسبي يُحفظ كما هو
        config["entry"],
        config["port"]
    ))

conn.commit()
conn.close()
print("✔ Database initialized and path saved as relative.")
