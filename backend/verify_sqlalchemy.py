from sqlalchemy import inspect

from app.database.connection import engine


database_inspector = inspect(engine)

tables = database_inspector.get_table_names()

print("\nSpendWise SQLAlchemy Database Verification")
print("------------------------------------------")

for table in tables:
    print(f"- {table}")

print(f"\nTotal tables: {len(tables)}")


expected_tables = {
    "users",
    "categories",
    "income",
    "expenses",
    "budgets",
    "debts",
    "repayments",
    "planned_expenses",
}

if expected_tables.issubset(set(tables)):
    print("\nSUCCESS: SQLAlchemy connected to the existing database.")

else:
    print("\nWARNING: Some expected tables are missing.")