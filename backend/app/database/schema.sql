-- =========================================
-- SPENDWISE DATABASE SCHEMA
-- =========================================

-- 1. USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- 2. CATEGORIES TABLE
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('income', 'expense')),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
);


-- 3. INCOME TABLE
CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    amount_minor INTEGER NOT NULL CHECK (amount_minor > 0),
    source TEXT NOT NULL,
    description TEXT,
    date_received DATE NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,

    FOREIGN KEY (category_id) REFERENCES categories(id)
);


-- 4. EXPENSES TABLE
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    amount_minor INTEGER NOT NULL CHECK (amount_minor > 0),
    description TEXT,
    date_spent DATE NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,

    FOREIGN KEY (category_id) REFERENCES categories(id)
);


-- 5. BUDGETS TABLE
CREATE TABLE IF NOT EXISTS budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    amount_minor INTEGER NOT NULL CHECK (amount_minor > 0),
    period TEXT NOT NULL CHECK (period = 'monthly'),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CHECK (start_date <= end_date),

    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,

    FOREIGN KEY (category_id) REFERENCES categories(id)
);


-- 6. DEBTS TABLE
CREATE TABLE IF NOT EXISTS debts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    person_name TEXT NOT NULL,
    direction TEXT NOT NULL CHECK (
        direction IN ('borrowed', 'lent')
    ),
    amount_minor INTEGER NOT NULL CHECK (amount_minor > 0),
    description TEXT,
    date_recorded DATE NOT NULL,
    due_date DATE,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (
        status IN ('pending', 'partially_paid', 'settled')
    ),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
);


-- 7. REPAYMENTS TABLE
CREATE TABLE IF NOT EXISTS repayments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    debt_id INTEGER NOT NULL,
    amount_minor INTEGER NOT NULL CHECK (amount_minor > 0),
    repayment_date DATE NOT NULL,
    description TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (debt_id) REFERENCES debts(id)
        ON DELETE CASCADE
);


-- 8. PLANNED EXPENSES TABLE
CREATE TABLE IF NOT EXISTS planned_expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    title TEXT NOT NULL,
    amount_minor INTEGER NOT NULL CHECK (amount_minor > 0),
    planned_date DATE NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'planned' CHECK (
        status IN ('planned', 'paid', 'cancelled')
    ),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,

    FOREIGN KEY (category_id) REFERENCES categories(id)
);


-- =========================================
-- INDEXES
-- =========================================

CREATE INDEX IF NOT EXISTS idx_income_user
ON income(user_id);

CREATE INDEX IF NOT EXISTS idx_income_date
ON income(date_received);

CREATE INDEX IF NOT EXISTS idx_expenses_user
ON expenses(user_id);

CREATE INDEX IF NOT EXISTS idx_expenses_date
ON expenses(date_spent);

CREATE INDEX IF NOT EXISTS idx_budgets_user
ON budgets(user_id);

CREATE INDEX IF NOT EXISTS idx_debts_user
ON debts(user_id);

CREATE INDEX IF NOT EXISTS idx_debts_due_date
ON debts(due_date);

CREATE INDEX IF NOT EXISTS idx_repayments_debt
ON repayments(debt_id);

CREATE INDEX IF NOT EXISTS idx_planned_user
ON planned_expenses(user_id);

CREATE INDEX IF NOT EXISTS idx_planned_date
ON planned_expenses(planned_date);