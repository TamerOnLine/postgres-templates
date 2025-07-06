import subprocess
import os
import sqlite3
import psutil
import time
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "projects.db")


def get_projects():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, type, path, entry, port FROM projects")
    projects = cursor.fetchall()
    conn.close()
    return projects


def is_port_in_use(port):
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == psutil.CONN_LISTEN and conn.laddr.port == port:
            return True
    return False


import subprocess
import os
import sqlite3
import psutil
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "projects.db")


def get_projects():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, type, path, entry, port FROM projects")
    projects = cursor.fetchall()
    conn.close()
    return projects


def is_port_in_use(port):
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == psutil.CONN_LISTEN and conn.laddr.port == port:
            return True
    return False


def find_process_using_port(port):
    for proc in psutil.process_iter(["pid", "name", "connections"]):
        try:
            for conn in proc.connections(kind="inet"):
                if conn.laddr.port == port:
                    return proc
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return None




def stop_project(project_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT pid FROM projects WHERE id = ?", (project_id,))
    result = cursor.fetchone()

    if not result or result[0] is None:
        return False, "❌ No PID found to stop."

    pid = result[0]
    try:
        p = psutil.Process(pid)
        p.terminate()  # or p.kill()
    except Exception as e:
        return False, f"❌ Failed to stop process: {e}"

    cursor.execute("UPDATE projects SET is_running = 0, pid = NULL WHERE id = ?", (project_id,))
    conn.commit()
    conn.close()
    return True, "✅ Project stopped."



def start_project(project_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT type, path, entry, port FROM projects WHERE id=?", (project_id,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return False, "❌ Project not found."

    type_, path, entry, port = result
    full_path = os.path.abspath(os.path.join(BASE_DIR, path, entry))

    if not os.path.exists(full_path):
        conn.close()
        return False, f"❌ Entry file not found: {full_path}"

    try:
        os.chdir(os.path.abspath(os.path.join(BASE_DIR, path)))

        if type_ in ["flask", "python"]:
            process = subprocess.Popen(["python", entry])
        elif type_ == "node":
            process = subprocess.Popen(["node", entry])
        elif type_ == "custom":
            process = subprocess.Popen(entry, shell=True)
        elif type_ == "html-server":
            os.chdir(entry)  # ← قد تحتاج إلى تحسين هذا لاحقًا
            process = subprocess.Popen(["python", "-m", "http.server", str(port)])
        else:
            conn.close()
            return False, f"❌ Unsupported project type: {type_}"

        # ✅ حفظ PID في قاعدة البيانات
        cursor.execute("UPDATE projects SET pid = ?, is_running = 1 WHERE id = ?", (process.pid, project_id))
        conn.commit()
        conn.close()

        return True, "✅ Project started successfully."
    
    except Exception as e:
        conn.close()
        return False, f"❌ Failed to start: {e}"



def restart_project(project_id):
    stopped, msg = stop_project(project_id)
    if stopped:
        time.sleep(1)
        return start_project(project_id)
    return False, msg


def add_project(name, type_, path, entry, port):
    # 🔐 التحقق من صحة البيانات أولًا
    if not all([name, type_, path, entry, port]):
        return False, "❌ All fields (name, type, path, entry, port) are required."

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM projects WHERE name = ?", (name,))
        if cursor.fetchone()[0] > 0:
            return False, "❌ Project already exists."

        cursor.execute("""
            INSERT INTO projects (name, type, path, entry, port)
            VALUES (?, ?, ?, ?, ?)
        """, (name, type_, path, entry, port))

        conn.commit()
        conn.close()
        return True, "✅ Project added successfully."
    except Exception as e:
        return False, f"❌ Error: {e}"



def delete_project(project_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id=?", (project_id,))
    conn.commit()
    conn.close()
    return True, "🗑️ Project deleted successfully."


def update_project(project_id, name, type_, path, entry, port):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE projects
        SET name=?, type=?, path=?, entry=?, port=?
        WHERE id=?
    """, (name, type_, path, entry, port, project_id))
    conn.commit()
    conn.close()
    return True, "✅ Project updated successfully."





def stop_project(project_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT pid FROM projects WHERE id = ?", (project_id,))
    result = cursor.fetchone()

    if not result or result[0] is None:
        return False, "❌ No PID found to stop."

    pid = result[0]
    try:
        p = psutil.Process(pid)
        p.terminate()  # or p.kill()
    except Exception as e:
        return False, f"❌ Failed to stop process: {e}"

    cursor.execute("UPDATE projects SET is_running = 0, pid = NULL WHERE id = ?", (project_id,))
    conn.commit()
    conn.close()
    return True, "✅ Project stopped."



def start_project(project_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT type, path, entry, port FROM projects WHERE id=?", (project_id,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return False, "❌ Project not found."

    type_, path, entry, port = result
    full_path = os.path.abspath(os.path.join(BASE_DIR, path, entry))

    if not os.path.exists(full_path):
        conn.close()
        return False, f"❌ Entry file not found: {full_path}"

    try:
        os.chdir(os.path.abspath(os.path.join(BASE_DIR, path)))

        if type_ in ["flask", "python"]:
            process = subprocess.Popen(["python", entry])
        elif type_ == "node":
            process = subprocess.Popen(["node", entry])
        elif type_ == "custom":
            process = subprocess.Popen(entry, shell=True)
        elif type_ == "html-server":
            os.chdir(entry)  # ← قد تحتاج إلى تحسين هذا لاحقًا
            process = subprocess.Popen(["python", "-m", "http.server", str(port)])
        else:
            conn.close()
            return False, f"❌ Unsupported project type: {type_}"

        # ✅ حفظ PID في قاعدة البيانات
        cursor.execute("UPDATE projects SET pid = ?, is_running = 1 WHERE id = ?", (process.pid, project_id))
        conn.commit()
        conn.close()

        return True, "✅ Project started successfully."
    
    except Exception as e:
        conn.close()
        return False, f"❌ Failed to start: {e}"



def restart_project(project_id):
    stopped, msg = stop_project(project_id)
    if stopped:
        time.sleep(1)
        return start_project(project_id)
    return False, msg


def add_project(name, type_, path, entry, port):
    # 🔐 التحقق من صحة البيانات أولًا
    if not all([name, type_, path, entry, port]):
        return False, "❌ All fields (name, type, path, entry, port) are required."

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM projects WHERE name = ?", (name,))
        if cursor.fetchone()[0] > 0:
            return False, "❌ Project already exists."

        cursor.execute("""
            INSERT INTO projects (name, type, path, entry, port)
            VALUES (?, ?, ?, ?, ?)
        """, (name, type_, path, entry, port))

        conn.commit()
        conn.close()
        export_projects_to_json()

        return True, "✅ Project added successfully."
    except Exception as e:
        return False, f"❌ Error: {e}"



def delete_project(project_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id=?", (project_id,))
    conn.commit()
    conn.close()
    

    return True, "🗑️ Project deleted successfully."


def update_project(project_id, name, type_, path, entry, port):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE projects
        SET name=?, type=?, path=?, entry=?, port=?
        WHERE id=?
    """, (name, type_, path, entry, port, project_id))
    conn.commit()
    conn.close()
    export_projects_to_json()

    return True, "✅ Project updated successfully."


def export_projects_to_json():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, type, path, entry, port FROM projects")
    rows = cursor.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "name": row[0],
            "type": row[1],
            "path": row[2],
            "entry": row[3],
            "port": row[4]
        })

    config_path = os.path.join(BASE_DIR, "serve-config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✅ serve-config.json updated.")
