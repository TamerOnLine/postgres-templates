import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

# 🚀 إعداد التطبيق
app = FastAPI()

# 🌍 تفعيل CORS (مفتوح للجميع حاليًا)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📁 إعداد المسارات
BASE_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# 🔍 استرجاع أسماء القوالب (المجلدات) المتوفرة
def get_available_templates():
    return [
        name for name in os.listdir(TEMPLATES_DIR)
        if os.path.isdir(os.path.join(TEMPLATES_DIR, name))
        and name != "j2"  # تجاهل مجلد j2
    ]

# 🏠 صفحة اختيار القوالب
@app.get("/", response_class=HTMLResponse)
def select_template_page(request: Request):
    available_templates = get_available_templates()
    return templates.TemplateResponse("select_template.html", {
        "request": request,
        "templates": available_templates
    })

# 👁️ عرض index.html داخل قالب معين
@app.get("/view/{template_name}", response_class=HTMLResponse)
def view_template(request: Request, template_name: str):
    index_path = os.path.join(TEMPLATES_DIR, template_name, "index.html")
    if not os.path.exists(index_path):
        return HTMLResponse(content=f"<h1>Template '{template_name}' not found.</h1>", status_code=404)

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content)

# 📂 خدمة الملفات الثابتة داخل كل قالب (CSS/JS)
@app.get("/static/{template_name}/{file_path:path}")
def serve_template_static(template_name: str, file_path: str):
    static_file = os.path.join(TEMPLATES_DIR, template_name, file_path)
    if not os.path.exists(static_file):
        return HTMLResponse(f"<h1>File not found: {file_path}</h1>", status_code=404)
    return FileResponse(static_file)

# 🧱 خدمة ملفات static داخل كل قالب
app.mount(
    "/template-static",
    StaticFiles(directory=os.path.join(BASE_DIR, "templates")),
    name="template_static"
)
