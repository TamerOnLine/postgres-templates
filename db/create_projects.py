def table_exists(cur, name):
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = %s
        );
    """, (name,))
    return cur.fetchone()[0]

def create_projects_table(cur):
    table_name = 'projects'
    exists = table_exists(cur, table_name)

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

    if exists:
        print(f"ℹ️ Table '{table_name}' already exists.")
    else:
        print(f"✅ Table '{table_name}' was created.")
