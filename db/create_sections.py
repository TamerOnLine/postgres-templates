def create_sections_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sections (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            print_visible BOOLEAN DEFAULT TRUE,
            order_index INTEGER DEFAULT 0
        );
    """)
