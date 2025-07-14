import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))             # serve-manager/
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))          # postgres-templates/
VENV_DIR = os.path.join(ROOT_DIR, "venv")                           # ← 🔁 البيئة الموحدة
MAIN_FILE = os.path.join(SCRIPT_DIR, "main.py")
INIT_SYSTEM = os.path.join(ROOT_DIR, "db", "init_system.py")

def run_init_system():
    print("🚀 Running init_system.py to initialize the database and tables...")
    subprocess.run(
        [os.path.join(VENV_DIR, "Scripts", "python"), INIT_SYSTEM],
        cwd=SCRIPT_DIR,
        check=True
    )

def run_server():
    """
    Runs the FastAPI app using uvicorn on http://127.0.0.1:5555.
    """
    uvicorn_path = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "uvicorn")
    print("Starting server at http://127.0.0.1:5555")
    subprocess.run(
        [uvicorn_path, "main:app", "--reload", "--port", "5555"],
        cwd=SCRIPT_DIR
    )

def main():
    run_init_system()
    run_server()

if __name__ == "__main__":
    main()
