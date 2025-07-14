import os
import sys

# ضمان عمل المسارات (حل مشكلة ModuleNotFoundError)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# (اختياري لتطوير اليدوي داخل serve-manager مباشرة)
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

from db_utils import get_template_settings, get_sections_with_projects, get_template_path
from fastapi.staticfiles import StaticFiles
from api.routes import sections
from api import user_resume_settings



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
#TEMPLATES_DIR = os.path.abspath(os.path.join(BASE_DIR, "../templates/two-column-dynamic"))

# 🚀 إنشاء تطبيق FastAPI
app = FastAPI()

# 📦 تحميل الملفات الثابتة والقوالب
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)
app.include_router(sections.router)
app.include_router(user_resume_settings.router)

# 🧱 دعم تحميل ملفات CSS/JS من داخل كل القوالب تحت templates/*
app.mount(
    "/templates",
    StaticFiles(directory=os.path.abspath(os.path.join(BASE_DIR, "..", "templates"))),
    name="templates"
)

# 🌐 إعداد CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import sqlite3
import os

def get_templates_list():
    db_path = os.path.join(os.path.dirname(__file__), "projects.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM projects")
    templates = cur.fetchall()
    conn.close()
    return templates



# 🏠 الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
def show_dashboard(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })



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
    


@app.get("/view/{template_id}", response_class=HTMLResponse)
def view_template(request: Request, template_id: int):
    user_id = 1
    print_settings = get_template_settings(user_id, template_id)
    sections = get_sections_with_projects(user_id)
    template_folder = get_template_path(template_id)

    dynamic_path = os.path.abspath(os.path.join(BASE_DIR, "..", "templates", template_folder))
    dynamic_templates = Jinja2Templates(directory=dynamic_path)

    return dynamic_templates.TemplateResponse("index.html", {
        "request": request,
        "print_settings": print_settings,
        "sections": sections,
        "template_folder": template_folder
    })
