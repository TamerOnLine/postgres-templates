# PostgreSQL Database System for Resume Templates

This directory (`db/`) contains everything related to setting up and managing the PostgreSQL database used in the resume template system.

## ✅ Features

- Automatic database creation if it doesn’t exist.
- SQLAlchemy ORM with declarative model structure.
- Alembic migrations for tracking schema changes.
- Custom per-user settings for templates, sections, items, and print options.
- Modular structure and portable integration.

---

## 📁 Structure

```plaintext
db/
├── alembic/                  # Alembic migration files
├── models/                   # SQLAlchemy models
│   ├── user.py
│   ├── template.py
│   ├── section.py
│   └── ...
├── config.py                 # Database connection configuration
├── setup.py                  # Virtual environment + installation + init + migrations
├── init_system.py            # Creates DB + runs Base.metadata.create_all()
├── requirements.txt
└── README.md                 # This file
```

---

## ⚙️ Setup Instructions

```bash
cd db
python setup.py
```

This will:

1. Create a virtual environment under `db/venv/` if not found.
2. Install required dependencies.
3. Initialize the PostgreSQL database and tables.
4. Run Alembic migrations.

---

## 🔄 Recreate Database

To drop and recreate the database:

```bash
python setup.py
# Choose: Drop → Create → Migrate
```

---

## 🛠️ Technologies Used

- PostgreSQL
- SQLAlchemy
- Alembic
- Python 3.12+
- dotenv (.env file support)

---

## 👤 Author-specific Settings

Each user can have:

- Global template print settings (`print_settings`)
- Element-specific print preferences (`user_project_settings`, `user_item_settings`, etc.)
- Full control over resume layout and visibility

---

## 📦 Deployment Note

This system is designed to be **portable**. You can embed it into any resume template project and it will auto-detect its context via paths and `.env`.