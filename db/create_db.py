import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# تحميل المتغيرات من ملف .env
load_dotenv()

# أخذ معلومات الاتصال من المتغيرات
db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")

# الاتصال بقاعدة postgres (القاعدة الأم)
conn = psycopg2.connect(
    dbname="postgres",  # لا يمكن الاتصال بقاعدة غير موجودة بعد
    user=user,
    password=password,
    host=host,
    port=port
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

# إنشاء قاعدة البيانات إذا لم تكن موجودة
cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (db_name,))
exists = cur.fetchone()

if not exists:
    cur.execute(f"CREATE DATABASE {db_name};")
    print(f"✅ تم إنشاء قاعدة البيانات: {db_name}")
else:
    print(f"ℹ️ قاعدة البيانات {db_name} موجودة مسبقًا.")

cur.close()
conn.close()
