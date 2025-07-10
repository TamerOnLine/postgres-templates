import os
import sys

# 🧠 ضمان استخدام البيئة الافتراضية عند الحاجة (اختياري ولكن مفيد للتطوير اليدوي)
venv_path = os.path.join(os.path.dirname(__file__), "venv", "Lib", "site-packages")
if venv_path not in sys.path:
    sys.path.insert(0, venv_path)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv

from controller import (
    get_projects,
    start_project,
    stop_project,
    restart_project,
    add_project,
    delete_project,
    is_port_in_use,
    get_db_connection  # ✅ أضف هذا
)


# 📁 تحميل المتغيرات البيئية
load_dotenv()

DB_PARAMS = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# 🗂️ إعداد المسارات
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# 🚀 إنشاء تطبيق FastAPI
app = FastAPI()

# 📦 تحميل الملفات الثابتة والقوالب
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# 🌐 إعداد CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🏠 الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 📄 عرض المشاريع
@app.get("/projects")
def list_projects():
    projects = get_projects()
    return [
        {
            "id": p[0],
            "name": p[1],
            "type": p[2],
            "port": p[5],
            "status": "Running" if is_port_in_use(p[5]) else "Stopped"
        }
        for p in projects
    ]

# ▶️ تشغيل مشروع
@app.post("/start/{project_id}")
def start(project_id: int):
    success, message = start_project(project_id)
    return {"status": "ok" if success else "error", "message": message}

# ⏹️ إيقاف مشروع
@app.post("/stop/{project_id}")
def stop(project_id: int):
    success = stop_project(project_id)
    return {"status": "ok" if success else "error", "message": "🛑 Stopped" if success else "❌ Not Found or Already Stopped"}

# 🔁 إعادة تشغيل مشروع
@app.post("/restart/{project_id}")
def restart(project_id: int):
    success, message = restart_project(project_id)
    return {"status": "ok" if success else "error", "message": message}

# ➕ إضافة مشروع
class ProjectData(BaseModel):
    name: str
    type: str
    path: str
    entry: str
    port: int

@app.post("/add")
def add(data: ProjectData):
    success, message = add_project(data.name, data.type, data.path, data.entry, data.port)
    return {"status": "ok" if success else "error", "message": message}

# ❌ حذف مشروع
@app.post("/delete/{project_id}")
def delete(project_id: int):
    success, message = delete_project(project_id)

    if success:
        from controller import save_config
        conn = get_db_connection()
        save_config(conn)
        conn.close()

    return {"status": "ok" if success else "error", "message": message}



@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    print_settings = get_print_settings()  # من controller
    return templates.TemplateResponse("index.html", {
        "request": request,
        "print_settings": print_settings
    })



# 🖨️ إعدادات الطباعة
@app.get("/api/print-settings")
def get_print_settings():
    try:
        with psycopg2.connect(**DB_PARAMS) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT element_id, font_family, font_size, line_height, margin_top, margin_bottom, visible
                    FROM print_settings;
                """)
                rows = cur.fetchall()

        result = [
            {
                "element_id": row[0],
                "font_family": row[1],
                "font_size": row[2],
                "line_height": row[3],
                "margin_top": row[4],
                "margin_bottom": row[5],
                "visible": row[6]
            }
            for row in rows
        ]
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})