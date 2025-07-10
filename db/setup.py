# db/setup.py

import os
import subprocess
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(SCRIPT_DIR, "venv")
REQUIREMENTS = os.path.join(SCRIPT_DIR, "requirements.txt")
INIT_SCRIPT = os.path.join(SCRIPT_DIR, "init_system.py")
PYTHON_EXE = sys.executable

def create_venv():
    print("📦 Creating virtual environment...")
    subprocess.run([PYTHON_EXE, "-m", "venv", VENV_DIR], check=True)

def install_requirements():
    pip_path = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "pip")
    print("📥 Installing packages from requirements.txt...")
    subprocess.run([pip_path, "install", "-r", REQUIREMENTS], check=True)

def run_init_script():
    python_path = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "python")
    print("🚀 Running init_system.py to initialize the database and tables...")
    subprocess.run([python_path, INIT_SCRIPT], cwd=SCRIPT_DIR, check=True)

def run_migrations():
    alembic_path = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "alembic")
    alembic_ini = os.path.join(SCRIPT_DIR, "alembic.ini")
    print("📜 Running Alembic migrations...")
    subprocess.run([alembic_path, "-c", alembic_ini, "upgrade", "head"], cwd=SCRIPT_DIR, check=True)


def main():
    os.chdir(SCRIPT_DIR)
    if not os.path.exists(VENV_DIR):
        create_venv()
        install_requirements()
    run_init_script()
    run_migrations()

if __name__ == "__main__":
    main()
