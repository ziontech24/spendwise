import sys
from pathlib import Path

from alembic import context

# Add the backend directory to Python's import path
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_DIR))

# Import SQLAlchemy database configuration
from app.database.base import Base
from app.database.connection import engine

# Import all models so SQLAlchemy registers their tables
import app.models


# Alembic configuration
config = context.config

# Use the existing SpendWise database connection
database_url = engine.url.render_as_string(
    hide_password=False
)

config.set_main_option(
    "sqlalchemy.url",
    database_url.replace("%", "%%"),
)
# Metadata containing all SQLAlchemy models
target_metadata = Base.metadata
def include_object(
    object,
    name,
    type_,
    reflected,
    compare_to,
):
    if type_ == "column" and name == "id":
        if object.primary_key:
            return False

    return True


def run_migrations_offline():
    """Run migrations without creating a database connection."""

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations using a live database connection."""

    with engine.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            render_as_batch=True,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()