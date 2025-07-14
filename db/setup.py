import os
import subprocess
import sys
import venv

# 🔧 اجعل المسارات تشير إلى الجذر الحقيقي للمشروع
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))  # ← مجلد postgres-templates
VENV_DIR = os.path.join(ROOT_DIR, "venv")
INIT_SYSTEM = os.path.join(SCRIPT_DIR, "init_system.py")  # موجود داخل db/
ALEMBIC_INI = os.path.join(SCRIPT_DIR, "alembic.ini")     # موجود داخل db/



def run_init_system():
    print("🚀 Running init_system.py to initialize the database and tables...")
    subprocess.run(
        [os.path.join(VENV_DIR, "Scripts", "python"), INIT_SYSTEM],
        cwd=SCRIPT_DIR,
        check=True
    )

def run_alembic_upgrade():
    print("📜 Running Alembic migrations...")
    subprocess.run(
        [os.path.join(VENV_DIR, "Scripts", "alembic"), "-c", ALEMBIC_INI, "upgrade", "head"],
        cwd=SCRIPT_DIR,
        check=True
    )

def main():
    run_init_system()
    run_alembic_upgrade()
    print("✅ Setup completed successfully.")

if __name__ == "__main__":
    main()
