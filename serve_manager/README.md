# 📂 serve-manager

A portable, self-contained server management module designed to control resume templates and associated data through a Flask-based web interface.

---

## 📌 Features

- 🔌 **Plug-and-play design** – portable inside any project.
- 🖥️ **Web control panel** – accessible via browser (Uvicorn/Flask).
- 🧩 **Dynamic routing** – serves templates and static files using `__file__`-based paths.
- 🧾 **Resume data management** – add/edit/delete projects, sections, items.
- ✍️ **Print settings control** – manage font, size, spacing, and margin per user/template.
- 🗃️ **JSON config integration** – reads from `serve-config.json` for environment setup.

---

## 📁 Directory Structure

```
serve-manager/
├── setup.py                 # Dynamic entry point
├── main.py                  # FastAPI app (optional Flask)
├── serve-config.json        # Contains selected template and environment setup
├── templates/
│   ├── static/              # Static JS, CSS, assets
│   └── index.html           # Main web UI
├── api/                     # Flask/FastAPI endpoints
│   ├── routes/              # Route handlers (e.g., projects, sections, items)
│   └── models/              # Data structures for requests/responses
├── db.sqlite                # Internal SQLite DB (for runtime cache if needed)
```

---

## ⚙️ Configuration: `serve-config.json`

```json
{
  "project_name": "tameronline-resume-templates",
  "default_template": "two-column-dynamic",
  "server_port": 5500,
  "database_type": "postgres",
  "external_db": true
}
```

---

## 🚀 How to Run

```bash
# Inside the serve-manager directory
python setup.py
```

By default, the server will run at [http://127.0.0.1:5500](http://127.0.0.1:5500) and load the interface to control templates and content dynamically.

---

## 🧠 Integration with Resume DB

- Loads templates from `templates/`
- Saves user-specific settings in a **PostgreSQL** database
- Supports per-user configuration for:
  - Visibility of sections/items
  - Print formatting per element
  - Template-specific adjustments

---

## 🧪 API Endpoints (Examples)

| Method | Endpoint         | Description                    |
|--------|------------------|--------------------------------|
| GET    | `/projects`      | Fetch all projects             |
| POST   | `/sections`      | Add a new section              |
| PUT    | `/items/{id}`    | Update item                    |
| DELETE | `/projects/{id}` | Delete project                 |

---

## ✅ Status

- ✅ Fully portable
- ✅ Template-aware
- ✅ Print-customizable
- ✅ Integrated with external DB