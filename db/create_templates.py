def table_exists(cur, name):
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = %s
        );
    """, (name,))
    return cur.fetchone()[0]

def create_templates_table(cur):
    table_name = 'templates'
    exists = table_exists(cur, table_name)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS templates (
            id SERIAL PRIMARY KEY,
            name TEXT,
            path TEXT,
            is_default BOOLEAN DEFAULT FALSE
        );
    """)

    if exists:
        print(f"ℹ️ Table '{table_name}' already exists.")
    else:
        print(f"✅ Table '{table_name}' was created.")
