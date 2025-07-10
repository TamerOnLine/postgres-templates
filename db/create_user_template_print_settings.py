def table_exists(cur, name):
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = %s
        );
    """, (name,))
    return cur.fetchone()[0]

def create_user_template_print_settings_table(cur):
    table_name = 'user_template_print_settings'
    exists = table_exists(cur, table_name)

    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
            template_id INTEGER REFERENCES templates(id) ON DELETE CASCADE,
            font_family TEXT DEFAULT 'Georgia',
            font_size TEXT DEFAULT '12pt',
            line_height TEXT DEFAULT '1.5',
            word_spacing TEXT DEFAULT '3pt',
            block_spacing TEXT DEFAULT '8px',
            margin_top TEXT DEFAULT '3cm',
            margin_bottom TEXT DEFAULT '3cm',
            margin_left TEXT DEFAULT '3cm',
            margin_right TEXT DEFAULT '3cm',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, template_id)
        );
    """)

    if exists:
        print(f"ℹ️ Table '{table_name}' already exists.")
    else:
        print(f"✅ Table '{table_name}' was created.")
