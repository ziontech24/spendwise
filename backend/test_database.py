from app.database.connection import engine


def test_database_insertion_and_retrieval():
    with engine.connect() as connection:
        transaction = connection.begin()

        try:
            # 1. Insert a test user
            result = connection.exec_driver_sql(
                """
                INSERT INTO users (username, email, password_hash)
                VALUES (?, ?, ?)
                """,
                (
                    "PytestUser",
                    "pytest-db-check@example.invalid",
                    "test_hash",
                ),
            )

            user_id = result.lastrowid

            # 2. Insert an expense category
            result = connection.exec_driver_sql(
                """
                INSERT INTO categories (user_id, name, type)
                VALUES (?, ?, ?)
                """,
                (user_id, "Pytest Food", "expense"),
            )

            category_id = result.lastrowid

            # 3. Insert an expense
            connection.exec_driver_sql(
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
                (
                    user_id,
                    category_id,
                    25000,
                    "Lunch",
                    "2026-11-06",
                ),
            )

            # 4. Retrieve the expense
            result = connection.exec_driver_sql(
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
                (user_id,),
            )

            expense = result.mappings().first()

            # 5. Verify the retrieved information
            assert expense is not None
            assert expense["description"] == "Lunch"
            assert expense["category"] == "Pytest Food"
            assert expense["amount_minor"] == 25000

        finally:
            # Undo test data so it doesn't remain in the database
            transaction.rollback()