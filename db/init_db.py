# db/init_db.py

import os
import sys
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Add project root to system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import table creation functions
from db.create_users import create_users_table
from db.create_projects import create_projects_table
from db.create_sections import create_sections_table
from db.create_items import create_items_table
from db.create_templates import create_templates_table
from db.create_print_settings import create_print_settings_table
from db.create_user_item_settings import create_user_item_settings_table
from db.create_user_project_settings import create_user_project_settings_table
from db.create_user_section_settings import create_user_section_settings_table
from create_user_template_print_settings import create_user_template_print_settings_table




def init_all_tables():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()

    # Table creation order matters
    create_users_table(cur)
    create_templates_table(cur)
    create_sections_table(cur)
    create_projects_table(cur)
    create_items_table(cur)
    create_print_settings_table(cur)
    create_user_item_settings_table(cur)
    create_user_project_settings_table(cur)
    create_user_section_settings_table(cur)
    create_user_template_print_settings_table(cur)
    
    conn.commit()
    cur.close()
    conn.close()
    print("✅ All tables were created successfully.")

# Run directly
if __name__ == "__main__":
    init_all_tables()
