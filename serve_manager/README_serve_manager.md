# 🚀 Serve Manager

This module runs the **FastAPI server** for managing and interacting with resume templates.

---

## 📁 Purpose

`serve-manager/` is the entry point for the backend web server of the resume management system.  
It serves the frontend, handles API routes, and connects to the centralized PostgreSQL database.

---

## ⚙️ Requirements

- Python 3.12+
- Unified virtual environment in the root folder: `postgres-templates/venv/`
- Database already initialized via `db/setup.py`

---

## ▶️ Running the Server

From the root of the project, execute:

```bash
python serve-manager/setup.py
```

This script will:

1. Ensure the database is initialized using `db/init_system.py`
2. Launch the FastAPI server using Uvicorn at:

```
http://127.0.0.1:5500
```

---

## 🧠 Notes

- All imports are based on a unified `PYTHONPATH` that includes:
  - `db/` → for models and config
  - `serve-manager/` → for routes and frontend files
- Make sure your IDE or VS Code is configured to recognize this Python path.
- The server auto-reloads when changes are detected in `serve-manager/`.

---

## 📦 Structure Overview

```plaintext
serve-manager/
├── api/                  # API routes (sections, projects, settings, etc.)
├── templates/            # Jinja2 templates for rendering HTML
├── static/               # Static files (JS, CSS, images)
├── main.py               # FastAPI app definition
├── setup.py              # Launches the server via uvicorn
└── ...
```

---

## 🧪 Development Tips

- For development mode, use:
  ```bash
  python serve-manager/setup.py
  ```
- To avoid `ModuleNotFoundError`, ensure `PYTHONPATH` includes both `db/` and `serve-manager/`.
- All server logs will be printed to the terminal where the script is run.

---

## 🔗 Related Modules

- [`db/`](../db/): Contains database models, migrations, and initialization logic.
- `venv/`: Shared virtual environment created at the project root.

---

## ✅ Status

This module is fully operational and ready for backend development or deployment.
