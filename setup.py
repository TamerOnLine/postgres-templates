import os
import subprocess
import sys
import webbrowser

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))        # ← جذر المشروع
DB_DIR = os.path.join(SCRIPT_DIR, "db")
INIT_SYSTEM = os.path.join(DB_DIR, "init_system.py")
VENV_DIR = os.path.join(SCRIPT_DIR, "venv")
VENV_PYTHON = os.path.join(VENV_DIR, "Scripts", "python")
UVICORN_PATH = os.path.join(VENV_DIR, "Scripts", "uvicorn")

def run_init_system():
    print("🚀 Running init_system.py to initialize the database and tables...")
    result = subprocess.run(
        [VENV_PYTHON, INIT_SYSTEM],
        cwd=DB_DIR
    )
    if result.returncode == 0:
        print("✅ Database initialized successfully.")
    else:
        print("❌ Failed to initialize database.")
        sys.exit(1)

def run_templates_server():
    print("🚀 Starting root template server...")
    subprocess.Popen(
        [UVICORN_PATH, "main:app", "--reload", "--port", "8000"],
        cwd=SCRIPT_DIR
    )
    print("✅ Server started successfully. Waiting for it to be ready...")

def open_templates_interface():
    url = "http://127.0.0.1:8000"
    print("🌐 Opening resume templates interface...")
    webbrowser.open(url)

def main():
    run_init_system()
    run_templates_server()
    open_templates_interface()
    print("✅ Project root setup completed.")

if __name__ == "__main__":
    main()
