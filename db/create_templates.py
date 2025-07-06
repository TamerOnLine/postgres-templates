def create_templates_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS templates (
            id SERIAL PRIMARY KEY,
            name TEXT,
            path TEXT,
            is_default BOOLEAN DEFAULT FALSE
        );
    """)
