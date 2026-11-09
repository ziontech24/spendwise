from app.database.connection import engine

with engine.connect() as connection:
    result = connection.exec_driver_sql(
        "PRAGMA foreign_keys"
    ).scalar()

    print("SpendWise Foreign Key Verification")
    print("----------------------------------")
    print(f"Foreign keys enabled: {result}")

    if result == 1:
        print("SUCCESS: Foreign-key enforcement is enabled.")
    else:
        print("WARNING: Foreign-key enforcement is disabled.")