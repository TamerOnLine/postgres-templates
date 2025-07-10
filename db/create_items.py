def table_exists(cur, name):
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = %s
        );
    """, (name,))
    return cur.fetchone()[0]

def create_items_table(cur):
    table_name = 'items'
    exists = table_exists(cur, table_name)

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

    if exists:
        print(f"ℹ️ Table '{table_name}' already exists.")
    else:
        print(f"✅ Table '{table_name}' was created.")
