# db/init_system.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.create_db import create_database_if_not_exists
# db/init_db.py

from db.models.base import Base
from db.config import engine

def init_all_tables():
    Base.metadata.create_all(engine)


def main():
    create_database_if_not_exists()
    init_all_tables()

if __name__ == "__main__":
    main()
