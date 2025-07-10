def table_exists(cur, name):
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = %s
        );
    """, (name,))
    return cur.fetchone()[0]

def create_user_section_settings_table(cur):
    table_name = 'user_section_settings'
    exists = table_exists(cur, table_name)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_section_settings (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
            section_id INTEGER REFERENCES sections(id) ON DELETE CASCADE,
            print_visible BOOLEAN DEFAULT TRUE,
            order_index INTEGER,
            UNIQUE(user_id, section_id)
        );
    """)

    if exists:
        print(f"ℹ️ Table '{table_name}' already exists.")
    else:
        print(f"✅ Table '{table_name}' was created.")
