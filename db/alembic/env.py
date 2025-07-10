from logging.config import fileConfig
import os
import sys

from sqlalchemy import engine_from_config, pool
from alembic import context

# ✳️ لإضافة مسار db/ إلى sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ✳️ تحميل متغيرات البيئة من .env
from dotenv import load_dotenv
load_dotenv()

# ✳️ توليد URI لقاعدة البيانات ديناميكيًا من البيئة
db_url = os.getenv("DATABASE_URL") or os.getenv("DB_URL") or (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME')}"
)

# ✳️ إعداد الكائن config
config = context.config
config.set_main_option("sqlalchemy.url", db_url)

# ✳️ إعداد ملف اللوج إذا كان معرفًا في alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✳️ تحميل جميع الجداول من models
from models import Base

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
