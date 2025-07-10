import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(SCRIPT_DIR, "venv")
REQUIREMENTS = os.path.join(SCRIPT_DIR, "requirements.txt")
MAIN_FILE = os.path.join(SCRIPT_DIR, "main.py")
PYTHON_EXE = sys.executable

def create_venv():
    """
    Creates a virtual environment in the SCRIPT_DIR/venv directory.
    """
    print("Creating virtual environment...")
    subprocess.run([PYTHON_EXE, "-m", "venv", VENV_DIR], check=True)

def install_requirements():
    """
    Installs required packages from requirements.txt using pip inside the virtual environment.
    """
    pip_path = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "pip")
    print("Installing requirements...")
    subprocess.run([pip_path, "install", "-r", REQUIREMENTS], check=True)

def run_server():
    """
    Runs the FastAPI app using uvicorn on http://127.0.0.1:5500.
    """
    uvicorn_path = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "uvicorn")
    print("Starting server at http://127.0.0.1:5500")
    subprocess.run(
        [uvicorn_path, "main:app", "--reload", "--port", "5500"],
        cwd=SCRIPT_DIR
    )

def main():
    """
    Main function to:
    - Ensure script is run from its directory
    - Create a virtual environment if not exists
    - Install requirements
    - Run the FastAPI server
    """
    os.chdir(SCRIPT_DIR)
    if not os.path.exists(VENV_DIR):
        create_venv()
        install_requirements()
    run_server()

if __name__ == "__main__":
    main()
