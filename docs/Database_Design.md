# SpendWise — Database Design

## 1. Introduction

This document describes the database design for SpendWise, a personalized financial management web application.

The database is designed to store and organize users' financial information, including income, expenses, budgets, borrowed and lent money, repayments, and planned expenses.

SpendWise will initially use SQLite as its relational database.

The design aims to maintain data consistency, minimize unnecessary duplication, and support future application expansion.

## 2. Database Technology

**Database Management System:** SQLite

SQLite is selected for the initial version because it is lightweight, simple to configure, and suitable for a small-scale personal finance application.

The database structure should also support a possible future migration to PostgreSQL.

## 3. Database Tables

The initial database will contain eight main tables:

1. users
2. categories
3. income
4. expenses
5. budgets
6. debts
7. repayments
8. planned_expenses

## 4. Table Definitions

### 4.1 Users Table

Stores user account information.

| Column | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | Primary Key | Unique user identifier |
| username | TEXT | NOT NULL | Display name |
| email | TEXT | UNIQUE, NOT NULL | User email |
| password_hash | TEXT | NOT NULL | Hashed password |
| created_at | DATETIME | NOT NULL | Account creation timestamp |

### 4.2 Categories Table

Stores income and expense categories.

| Column | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | Primary Key | Unique category identifier |
| user_id | INTEGER | Foreign Key, NULL allowed | Owner of custom category |
| name | TEXT | NOT NULL | Category name |
| type | TEXT | NOT NULL | Income or expense |
| created_at | DATETIME | NOT NULL | Creation timestamp |

Default categories may have a NULL user_id, while custom categories belong to a specific user.

### 4.3 Income Table

Stores income transactions.

| Column | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | Primary Key | Unique income identifier |
| user_id | INTEGER | Foreign Key, NOT NULL | Associated user |
| category_id | INTEGER | Foreign Key, NOT NULL | Income category |
| amount_minor | INTEGER | NOT NULL, positive | Amount in minor currency units |
| source | TEXT | NOT NULL | Income source |
| description | TEXT | NULL allowed | Additional details |
| date_received | DATE | NOT NULL | Date income was received |
| created_at | DATETIME | NOT NULL | Record creation timestamp |

### 4.4 Expenses Table

Stores expense transactions.

| Column | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | Primary Key | Unique expense identifier |
| user_id | INTEGER | Foreign Key, NOT NULL | Associated user |
| category_id | INTEGER | Foreign Key, NOT NULL | Expense category |
| amount_minor | INTEGER | NOT NULL, positive | Amount in minor currency units |
| description | TEXT | NULL allowed | Additional details |
| date_spent | DATE | NOT NULL | Date expense occurred |
| created_at | DATETIME | NOT NULL | Record creation timestamp |

### 4.5 Budgets Table

Stores overall and category-based budgets.

| Column | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | Primary Key | Unique budget identifier |
| user_id | INTEGER | Foreign Key, NOT NULL | Associated user |
| category_id | INTEGER | Foreign Key, NULL allowed | Budget category |
| amount_minor | INTEGER | NOT NULL, positive | Budget amount |
| period | TEXT | NOT NULL | Budget period |
| start_date | DATE | NOT NULL | Budget starting date |
| end_date | DATE | NOT NULL | Budget ending date |
| created_at | DATETIME | NOT NULL | Record creation timestamp |

A NULL category_id represents an overall budget.

A category_id represents a budget for a particular spending category.

The initial implementation will support monthly budgets.

### 4.6 Debts Table

Stores money borrowed from or lent to other people.

| Column | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | Primary Key | Unique debt identifier |
| user_id | INTEGER | Foreign Key, NOT NULL | Associated user |
| person_name | TEXT | NOT NULL | Other person's name |
| direction | TEXT | NOT NULL | Borrowed or lent |
| amount_minor | INTEGER | NOT NULL, positive | Original amount |
| description | TEXT | NULL allowed | Additional details |
| date_recorded | DATE | NOT NULL | Date borrowed or lent |
| due_date | DATE | NULL allowed | Expected repayment date |
| status | TEXT | NOT NULL | Current repayment status |
| created_at | DATETIME | NOT NULL | Record creation timestamp |

The direction field has two possible values:

- borrowed: The user owes money to another person.
- lent: Another person owes money to the user.

The status field may contain:

- pending
- partially_paid
- settled

The remaining balance will be calculated using the original amount and recorded repayments.

### 4.7 Repayments Table

Stores repayment transactions associated with debts.

| Column | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | Primary Key | Unique repayment identifier |
| debt_id | INTEGER | Foreign Key, NOT NULL | Associated debt |
| amount_minor | INTEGER | NOT NULL, positive | Repayment amount |
| repayment_date | DATE | NOT NULL | Repayment date |
| description | TEXT | NULL allowed | Additional details |
| created_at | DATETIME | NOT NULL | Record creation timestamp |

A debt can have multiple repayment records.

The total repaid amount is calculated by summing its repayment records.

The outstanding balance is:

Outstanding Balance = Original Debt Amount - Total Repayments

The backend must prevent repayment totals from exceeding the original debt amount.

### 4.8 Planned Expenses Table

Stores expenses expected to occur in the future.

| Column | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | Primary Key | Unique planned expense identifier |
| user_id | INTEGER | Foreign Key, NOT NULL | Associated user |
| category_id | INTEGER | Foreign Key, NULL allowed | Expense category |
| title | TEXT | NOT NULL | Planned expense title |
| amount_minor | INTEGER | NOT NULL, positive | Expected amount |
| planned_date | DATE | NOT NULL | Expected payment date |
| description | TEXT | NULL allowed | Additional details |
| status | TEXT | NOT NULL | Planned, paid, or cancelled |
| created_at | DATETIME | NOT NULL | Record creation timestamp |

A planned expense is not automatically considered a completed expense.

When the user makes the payment, an actual expense record should be created separately.

## 5. Database Relationships

The database will use primary keys and foreign keys to establish relationships.

| Parent Table | Child Table | Relationship |
|---|---|---|
| users | income | One-to-many |
| users | expenses | One-to-many |
| users | categories | One-to-many |
| users | budgets | One-to-many |
| users | debts | One-to-many |
| users | planned_expenses | One-to-many |
| categories | income | One-to-many |
| categories | expenses | One-to-many |
| categories | budgets | One-to-many |
| categories | planned_expenses | One-to-many |
| debts | repayments | One-to-many |

Each financial record belongs to one user.

A repayment belongs to one debt, while a debt can have multiple repayments.

## 6. Monetary Data Representation

SpendWise must handle financial calculations accurately.

Monetary amounts will be stored as integers representing minor currency units.

For Ethiopian Birr:

1 ETB = 100 cents.

Example:

5,000 ETB will be stored as 500,000 minor units.

The frontend will display monetary values in the appropriate currency format, while the backend handles the conversion and calculations.

Floating-point arithmetic should not be used for financial calculations.

## 7. Database Integrity and Constraints

The database will use appropriate constraints to maintain data consistency.

Important rules include:

- Every record must have a unique primary key.
- Financial records must reference valid users.
- Category references must point to valid categories belonging to the same user or available default categories.
- Monetary amounts must be positive.
- Debt direction must be either borrowed or lent.
- Repayment amounts must be positive.
- Repayment totals must not exceed the original debt amount.
- Budget start dates must not be later than end dates.
- Foreign-key enforcement must be enabled in SQLite.

The backend will perform additional validation before database operations.

## 8. Indexing

Indexes will be introduced to improve query performance.

Potential indexes include:

- income.user_id
- income.date_received
- expenses.user_id
- expenses.date_spent
- budgets.user_id
- debts.user_id
- debts.due_date
- repayments.debt_id
- planned_expenses.user_id
- planned_expenses.planned_date

Indexes will help retrieve financial records efficiently, especially when filtering by user and date.

## 9. Data Access and Security

Financial information must remain associated with its owner.

The backend must verify the authenticated user's identity before retrieving, updating, or deleting financial records.

Users must not be able to access another user's financial information by changing record identifiers.

Passwords must never be stored in plain text.

Database access will be handled through the backend rather than directly through the frontend.

## 10. Example Database Scenarios

### Scenario 1: Recording an Expense

A user spends 250 ETB on food.

The application creates a record in the expenses table containing:

- User ID
- Category ID
- Amount: 25,000 minor units
- Description
- Expense date

### Scenario 2: Creating a Monthly Budget

A user creates an overall monthly budget of 8,000 ETB.

The application stores:

- User ID
- Category ID: NULL
- Budget amount: 800,000 minor units
- Period: monthly
- Start date
- End date

### Scenario 3: Recording Borrowed Money

A user borrows 1,000 ETB from a friend.

The debts table stores:

- User ID
- Person name
- Direction: borrowed
- Amount: 100,000 minor units
- Status: pending

The user later repays 400 ETB.

A repayment record is created.

The remaining balance becomes 600 ETB.

### Scenario 4: Recording Lent Money

A user lends 2,000 ETB to another person.

The debts table stores:

- User ID
- Person name
- Direction: lent
- Amount: 200,000 minor units
- Status: pending

When the other person returns 500 ETB, a repayment record is created.

The remaining amount owed to the user becomes 1,500 ETB.

## 11. Future Database Improvements

Future versions may introduce:

- Savings goals.
- Recurring transactions.
- More advanced notification records.
- Financial report storage where necessary.
- Multiple currencies.
- Additional financial planning features.

The database may also be migrated from SQLite to PostgreSQL as the application grows.

## 12. Conclusion

The SpendWise database uses a relational structure with eight main tables.

The design separates financial transactions, budgets, debts, repayments, and planned expenses while maintaining clear relationships between records.

It provides a foundation for accurate financial calculations, secure data management, and future application expansion.