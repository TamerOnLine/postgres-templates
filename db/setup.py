import os
import subprocess
import sys
import venv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VENV_DIR = os.path.join(BASE_DIR, "venv")
REQUIREMENTS_FILE = os.path.join(BASE_DIR, "requirements.txt")
INIT_SYSTEM = os.path.join(BASE_DIR, "init_system.py")
ALEMBIC_INI = os.path.join(BASE_DIR, "alembic.ini")

def create_virtualenv():
    if not os.path.exists(VENV_DIR):
        print("📦 Creating virtual environment...")
        venv.create(VENV_DIR, with_pip=True)
    else:
        print("📦 Virtual environment already exists.")

def install_requirements():
    print("📥 Installing packages from requirements.txt...")
    subprocess.run(
        [os.path.join(VENV_DIR, "Scripts", "pip"), "install", "-r", REQUIREMENTS_FILE],
        check=True
    )

def run_init_system():
    print("🚀 Running init_system.py to initialize the database and tables...")
    subprocess.run(
        [os.path.join(VENV_DIR, "Scripts", "python"), INIT_SYSTEM],
        cwd=BASE_DIR,
        check=True
    )

def run_alembic_upgrade():
    print("📜 Running Alembic migrations...")
    subprocess.run(
        [os.path.join(VENV_DIR, "Scripts", "alembic"), "-c", ALEMBIC_INI, "upgrade", "head"],
        cwd=BASE_DIR,
        check=True
    )

def main():
    create_virtualenv()
    install_requirements()
    run_init_system()
    run_alembic_upgrade()
    print("✅ Setup completed successfully.")

if __name__ == "__main__":
    main()
