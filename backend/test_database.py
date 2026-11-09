from app.database.connection import get_connection


db = get_connection()

try:
    # Start a database transaction
    db.execute("BEGIN")

    # 1. Insert a test user
    db.execute(
        """
        INSERT INTO users (username, email, password_hash)
        VALUES (?, ?, ?)
        """,
        ("TestUser", "test@example.com", "test_hash")
    )

    user_id = db.execute(
        "SELECT id FROM users WHERE email = ?",
        ("test@example.com",)
    ).fetchone()["id"]

    # 2. Insert an expense category
    db.execute(
        """
        INSERT INTO categories (user_id, name, type)
        VALUES (?, ?, ?)
        """,
        (user_id, "Food", "expense")
    )

    category_id = db.execute(
        "SELECT id FROM categories WHERE name = ? AND user_id = ?",
        ("Food", user_id)
    ).fetchone()["id"]

    # 3. Insert an expense
    db.execute(
        """
        INSERT INTO expenses (
            user_id,
            category_id,
            amount_minor,
            description,
            date_spent
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, category_id, 25000, "Lunch", "2026-11-06")
    )

    # 4. Retrieve the expense
    expense = db.execute(
        """
        SELECT
            expenses.amount_minor,
            expenses.description,
            categories.name AS category
        FROM expenses
        JOIN categories
            ON expenses.category_id = categories.id
        WHERE expenses.user_id = ?
        """,
        (user_id,)
    ).fetchone()

    print("Database insertion and retrieval successful!")
    print(f"Description: {expense['description']}")
    print(f"Category: {expense['category']}")
    print(f"Amount: {expense['amount_minor'] / 100:.2f} ETB")

finally:
    # Undo test data so it doesn't remain in your database
    db.rollback()
    db.close()