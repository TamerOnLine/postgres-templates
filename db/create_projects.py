def create_projects_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id SERIAL PRIMARY KEY,
            section_id INTEGER REFERENCES sections(id) ON DELETE CASCADE,
            title TEXT,
            description TEXT,
            company TEXT,
            link TEXT,
            from_date TEXT,
            to_date TEXT,
            print_visible BOOLEAN DEFAULT TRUE,
            print_font_size TEXT DEFAULT '12pt',
            print_line_height TEXT DEFAULT '1.2',
            order_index INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
