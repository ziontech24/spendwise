from app.database.connection import get_connection

db = get_connection()

try:
    tables = db.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        AND name NOT LIKE 'sqlite_%'
        """
    ).fetchall()

    print("\nSpendWise Database Tables:")

    for table in tables:
        print(f"- {table['name']}")

    print(f"\nTotal tables: {len(tables)}")

finally:
    db.close()