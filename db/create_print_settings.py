def create_print_settings_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS print_settings (
            id SERIAL PRIMARY KEY,
            element_id TEXT NOT NULL UNIQUE,
            font_family TEXT DEFAULT 'Georgia',
            font_size TEXT DEFAULT '12pt',
            line_height TEXT DEFAULT '1.5',
            margin_top TEXT DEFAULT '0',
            margin_bottom TEXT DEFAULT '0',
            visible BOOLEAN DEFAULT TRUE
        );
    """)
