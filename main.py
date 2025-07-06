import os
import subprocess

def run_serve_manager():
    path = os.path.join("serve-manager", "main.py")
    subprocess.run(["python", path])

if __name__ == "__main__":
    print("🚀 Launching the serve-manager...")
    run_serve_manager()

import sys

def init_database():
    subprocess.run(["python", os.path.join("db", "init_db.py")])

if __name__ == "__main__":
    if "--init-db" in sys.argv:
        init_database()
    else:
        run_serve_manager()
