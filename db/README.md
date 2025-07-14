# 🗄️ DB System – Setup & Migration Guide

This module handles all database-related operations including schema creation, Alembic migrations, and initialization scripts.

---

## 📦 Requirements
- Python 3.11+
- PostgreSQL running and accessible
- The project-wide virtual environment is already created in: `postgres-templates/venv/`
- Environment variables configured in `.env`

---

## 📁 Structure

```
db/
├── alembic/                  ← Alembic migration versions
├── alembic.ini               ← Alembic config file
├── init_system.py            ← Initializes the database tables and defaults
├── setup.py                  ← Runs full DB setup and migration
├── config.py                 ← Loads DB settings from .env
├── models/                   ← SQLAlchemy model definitions
```

---

## ⚙️ Setup Instructions

### 1. Activate the project-wide virtual environment

```bash
# Windows
.\serve-manager\env\Scripts\ctivate

# Linux/macOS
source serve-manager/venv/bin/activate
```

---

### 2. Run the setup script

```bash
python db/setup.py
```

This script will:
- Run `init_system.py` to initialize core tables
- Execute Alembic migrations to bring the schema up to date

---

## 🛠️ Manual commands (if needed)

### Run Alembic manually

```bash
alembic -c db/alembic.ini upgrade head
```

### Run initialization manually

```bash
python db/init_system.py
```

---

## ✅ Notes

- This DB system **uses the shared virtual environment at the project root**.
- You **do not need to create a separate venv inside `db/`**.
- Ensure database credentials are valid and reachable from `.env`.