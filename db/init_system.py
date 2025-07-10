# db/init_system.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.create_db import create_database_if_not_exists
from db.init_db import init_all_tables

def main():
    create_database_if_not_exists()
    init_all_tables()

if __name__ == "__main__":
    main()
