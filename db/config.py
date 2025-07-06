# db/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # تحميل متغيرات .env

DB_URL = os.getenv("DATABASE_URL")
