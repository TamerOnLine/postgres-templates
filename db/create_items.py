def create_items_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            section_id INTEGER REFERENCES sections(id) ON DELETE CASCADE,
            label TEXT,
            value TEXT,
            print_visible BOOLEAN DEFAULT TRUE,
            print_font_size TEXT DEFAULT '12pt',
            order_index INTEGER DEFAULT 0
        );
    """)
