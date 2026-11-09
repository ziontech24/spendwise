from sqlalchemy import inspect
from sqlalchemy.orm import configure_mappers

from app.database.base import Base
from app.database.connection import engine
from app.models import User, Category


# Configure relationships between models
configure_mappers()

# Get tables recognized by SQLAlchemy
model_tables = set(Base.metadata.tables.keys())

# Get tables from the existing SQLite database
database_inspector = inspect(engine)
database_tables = set(database_inspector.get_table_names())

print("\nSpendWise Model Verification")
print("-----------------------------")

print("\nSQLAlchemy Models:")
for table in sorted(model_tables):
    print(f"- {table}")

print("\nExisting Database Tables:")
for table in sorted(model_tables):
    if table in database_tables:
        print(f"- {table}: FOUND")
    else:
        print(f"- {table}: MISSING")

# Verify that the model columns match the existing database columns
print("\nColumn Verification:")

for table in sorted(model_tables):
    model_columns = set(Base.metadata.tables[table].columns.keys())

    database_columns = {
        column["name"]
        for column in database_inspector.get_columns(table)
    }

    if model_columns == database_columns:
        print(f"- {table}: All columns match")
    else:
        print(f"- {table}: Column mismatch")
        print(f"  Missing in database: {model_columns - database_columns}")
        print(f"  Missing in model: {database_columns - model_columns}")

if model_tables.issubset(database_tables):
    print("\nSUCCESS: SQLAlchemy models recognize the existing database tables.")
else:
    print("\nWARNING: Some model tables are missing from the database.")