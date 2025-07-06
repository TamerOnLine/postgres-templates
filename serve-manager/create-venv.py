import subprocess
import os
import shutil

# 🧭 تحديد المجلد الذي فيه هذا السكربت
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def setup_env(env_name, python_version, requirements_filename=None):
    env_dir = os.path.join(BASE_DIR, env_name)
    requirements_file = os.path.join(BASE_DIR, requirements_filename) if requirements_filename else None

    # 🧹 إزالة البيئة القديمة إن وجدت
    if os.path.exists(env_dir):
        print(f"\n🧹 Removing existing virtual environment: {env_dir}")
        shutil.rmtree(env_dir)

    # 🆕 إنشاء البيئة الافتراضية
    print(f"🆕 Creating virtual environment ({env_dir}) with Python {python_version}")
    subprocess.run(["py", f"-{python_version}", "-m", "venv", env_dir], check=True)

    # 🔍 تحديد المسارات
    if os.name == "nt":
        pip_path = os.path.join(env_dir, "Scripts", "pip.exe")
        python_path = os.path.join(env_dir, "Scripts", "python.exe")
    else:
        pip_path = os.path.join(env_dir, "bin", "pip")
        python_path = os.path.join(env_dir, "bin", "python")

    # ⬆️ ترقية pip
    print("⬆️ Upgrading pip...")
    subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)

    # 📦 عرض الإصدارات
    subprocess.run([python_path, "--version"])
    subprocess.run([pip_path, "--version"])

    # 📦 تثبيت الحزم المطلوبة
    if requirements_file and os.path.exists(requirements_file):
        print(f"📦 Installing packages from {requirements_file}...")
        subprocess.run([pip_path, "install", "-r", requirements_file], check=True)
    else:
        print(f"⚠️ No {requirements_filename} file found or not specified.")

# ✅ إعداد البيئة الافتراضية داخل مجلد السكربت نفسه
setup_env("venv", "3.12", "requirements.txt")
#setup_env("venv_dev", "3.12", "Dev_requirements.txt")
#setup_env("venv_docs", "3.12", "gh-pages-requirements.txt")
