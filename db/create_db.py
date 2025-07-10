# db/create_db.py

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Load environment variables from .env file
load_dotenv()

def create_database_if_not_exists():
    # Read connection parameters from environment variables
    db_name = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")

    # Connect to the default 'postgres' database
    conn = psycopg2.connect(
        dbname="postgres",  # Connect to default DB first
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    # Check if the target database already exists
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (db_name,))
    exists = cur.fetchone()

    if not exists:
        cur.execute(f"CREATE DATABASE {db_name};")
        print(f"✅ Database '{db_name}' created successfully.")
    else:
        print(f"ℹ️ Database '{db_name}' already exists.")

    cur.close()
    conn.close()

# Run directly
if __name__ == "__main__":
    create_database_if_not_exists()
