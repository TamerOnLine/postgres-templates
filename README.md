# 🧠 Resume Template Manager – Setup Guide

## 🚀 Requirements
- Python 3.11+
- PostgreSQL installed and running
- `.env` file configured with database credentials

---

## 📁 Project Structure

```
postgres-templates/
├── db/
│   ├── setup.py               ← Runs DB setup and Alembic migrations
│   ├── init_system.py         ← Initializes core tables and defaults
│   ├── alembic.ini
│   └── alembic/
├── serve-manager/
│   ├── main.py                ← FastAPI app entry point
│   └── venv/                  ← Main and only virtual environment
├── requirements.txt
└── setup-config.json
```

---

## ⚙️ Setup Instructions

### 1. Activate the virtual environment

```bash
# Windows
.\serve-managerenv\Scriptsctivate

# Linux/macOS
source serve-manager/venv/bin/activate
```

---

### 2. Initialize the database and run Alembic migrations

```bash
python db/setup.py
```

This script:
- Runs `init_system.py`
- Applies Alembic migrations
- Uses the unified virtual environment at `serve-manager/venv`

---

### 3. Start the development server

```bash
uvicorn serve-manager.main:app --reload --port 8000
```

---

## ✅ Notes

- All systems use a **single unified virtual environment**.
- No need to create separate `venv` folders in `db` or elsewhere.
- Project is configured for real-server behavior in VS Code using `.vscode/settings.json` and `launch.json`.

---