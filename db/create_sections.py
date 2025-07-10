def table_exists(cur, name):
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = %s
        );
    """, (name,))
    return cur.fetchone()[0]

def create_sections_table(cur):
    table_name = 'sections'
    exists = table_exists(cur, table_name)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sections (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
            title TEXT,
            order_index INTEGER DEFAULT 0
        );
    """)

    if exists:
        print(f"ℹ️ Table '{table_name}' already exists.")
    else:
        print(f"✅ Table '{table_name}' was created.")
