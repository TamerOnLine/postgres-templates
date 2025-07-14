import sqlite3

# الاتصال بقاعدة البيانات الصحيحة
conn = sqlite3.connect("serve_manager/projects.db")
cursor = conn.cursor()

# تحديث مسار القالب من './templates/...' إلى 'two-column-dynamic' فقط
cursor.execute("""
UPDATE projects
SET path = 'two-column-dynamic'
WHERE id = 1
""")

conn.commit()
conn.close()

print("✅ تم تحديث المسار بنجاح.")
