# SpendWise — System Architecture

## 1. Introduction

This document describes the system architecture of SpendWise, a personalized financial management web application.

It explains the application's major components, their responsibilities, communication methods, database structure, and technology choices.

The architecture is designed to support modular development, maintainability, security, and future expansion.

## 2. Architectural Overview

SpendWise will follow a three-layer architecture consisting of:

1. Presentation Layer (Frontend)
2. Application Layer (Backend)
3. Data Layer (Database)

The frontend communicates with the backend through REST APIs. The backend processes requests, applies business rules, and communicates with the database.

### 2.1 High-Level Architecture

```text
                    USER
                      |
                      v
             PRESENTATION LAYER
                React Frontend
                      |
                 REST API
                      |
                      v
             APPLICATION LAYER
                FastAPI Backend
                      |
          -------------------------
          |           |           |
          v           v           v
       Income      Budget      Expense
       Service     Service     Service
          |           |           |
          -------------------------
                      |
                      v
                DATA LAYER
                 SQLite
                      |
          -------------------------
          |           |           |
          v           v           v
        Income     Expenses    Budgets
         Table      Table       Table
```

## 3. Presentation Layer — Frontend

### 3.1 Technology

- React.js
- JavaScript
- CSS

### 3.2 Responsibilities

The frontend provides the user interface and allows users to interact with SpendWise.

Its responsibilities include:

- Displaying the personalized dashboard.
- Collecting income and expense information.
- Displaying financial summaries.
- Managing budgets.
- Displaying daily spending recommendations.
- Managing borrowed and lent money.
- Recording repayments.
- Managing planned expenses.
- Displaying reminders.
- Providing an interactive financial question interface.

### 3.3 Frontend Structure

```text
frontend/
│
├── public/
│
├── src/
│   ├── assets/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   ├── styles/
│   ├── App.jsx
│   └── main.jsx
│
└── package.json
```

### 3.4 Frontend Responsibilities by Directory

| Directory | Responsibility |
|---|---|
| assets | Images, icons, and static resources. |
| components | Reusable interface components. |
| pages | Main application pages. |
| services | API communication functions. |
| hooks | Reusable React hooks. |
| styles | CSS and visual styling. |

The frontend will not communicate directly with the database. All financial operations will be handled through the backend API.

## 4. Application Layer — Backend

### 4.1 Technology

- Python
- FastAPI
- Pydantic

### 4.2 Responsibilities

The backend handles the application's business logic and data processing.

Its responsibilities include:

- Receiving frontend API requests.
- Validating submitted information.
- Processing income and expense records.
- Calculating financial summaries.
- Managing budgets.
- Calculating daily spending recommendations.
- Managing debts and repayments.
- Processing planned expenses.
- Generating dashboard information.
- Answering predefined financial questions.
- Communicating with the database.

### 4.3 Backend Structure

```text
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── routes/
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   ├── core/
│   │
│   └── database/
│
└── tests/
```

### 4.4 Backend Directory Responsibilities

| Directory | Responsibility |
|---|---|
| api/routes | Defines API endpoints and handles HTTP requests. |
| models | Defines database models and relationships. |
| schemas | Validates request and response data. |
| services | Implements business logic and calculations. |
| core | Stores configuration and security-related functionality. |
| database | Handles database connections and initialization. |
| tests | Contains backend tests. |

### 4.5 Service Modules

The backend will use separate service modules for major features.

| Service | Responsibility |
|---|---|
| Income Service | Manages income records. |
| Expense Service | Manages expense records. |
| Budget Service | Calculates and monitors budgets. |
| Spending Service | Calculates recommended daily spending. |
| Debt Service | Manages borrowed and lent money. |
| Dashboard Service | Generates financial summaries. |

Additional services can be introduced as the application develops.

## 5. Data Layer — Database

### 5.1 Technology

SQLite will be used as the initial database.

### 5.2 Responsibilities

The database stores and organizes the application's financial information.

### 5.3 Main Database Tables

| Table | Description |
|---|---|
| users | Stores user account information. |
| income | Stores income transactions. |
| expenses | Stores expense transactions. |
| budgets | Stores monthly and category-based budgets. |
| debts | Stores borrowed and lent money. |
| repayments | Stores repayment transactions. |
| planned_expenses | Stores planned future expenses. |

### 5.4 Database Relationships

- A user can have multiple income records.
- A user can have multiple expense records.
- A user can create multiple budgets.
- A user can have multiple debt records.
- A debt can have multiple repayment records.
- A user can create multiple planned expenses.

Financial records will be associated with their respective user accounts.

### 5.5 Financial Data Handling

Financial calculations must be accurate and consistent.

The backend should avoid ordinary floating-point arithmetic for monetary calculations. Appropriate decimal or integer-based monetary representations will be used.

Outstanding debt balances will be calculated using the original amount and recorded repayments.

Money owed to the user will not automatically be included in available cash.

## 6. Frontend and Backend Communication

The frontend and backend will communicate through REST APIs using HTTP requests.

### 6.1 HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve information. |
| POST | Create new records. |
| PUT | Update existing records. |
| DELETE | Delete records. |

### 6.2 Proposed API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| /api/income | GET | Retrieve income records. |
| /api/income | POST | Create an income record. |
| /api/expenses | GET | Retrieve expense records. |
| /api/expenses | POST | Create an expense record. |
| /api/budgets | GET | Retrieve budgets. |
| /api/budgets | POST | Create a budget. |
| /api/debts | GET | Retrieve debt records. |
| /api/debts | POST | Create a debt record. |
| /api/repayments | POST | Record a repayment. |
| /api/planned-expenses | GET | Retrieve planned expenses. |
| /api/dashboard | GET | Retrieve dashboard information. |
| /api/questions | POST | Process a predefined financial question. |

These endpoints represent the initial API design and may be refined during implementation.

## 7. Example Data Flow

### 7.1 Recording an Expense

When a user records a new expense:

1. The user enters the expense information in the React frontend.
2. The frontend sends a POST request to the backend.
3. FastAPI receives and validates the submitted information.
4. The expense service processes the request.
5. The backend saves the expense in SQLite.
6. The backend returns a response.
7. The frontend updates the expense list and relevant dashboard information.

### 7.2 Calculating Daily Spending Recommendations

1. The frontend requests a spending recommendation.
2. The backend retrieves the relevant budget information.
3. The spending service calculates the remaining budget.
4. The service considers the remaining days in the budget period and recorded planned expenses.
5. The backend returns the recommended daily spending amount and an explanation.
6. The frontend displays the recommendation.

The recommendation is intended to guide users rather than restrict their spending.

## 8. Security and Privacy Architecture

SpendWise will follow security and privacy-conscious development practices.

Important considerations include:

- User authentication and authorization.
- Validation of incoming data.
- Protection of sensitive financial information.
- Secure password storage if passwords are implemented.
- Avoiding unnecessary collection of personal information.
- Preventing users from accessing other users' financial records.
- Avoiding exposure of sensitive information in application logs.
- Secure handling of API requests.
- Appropriate error handling.

Authentication and authorization must be implemented before exposing personal financial data to multiple users.

## 9. Error Handling and Validation

The backend will validate incoming information before processing it.

Examples include:

- Rejecting invalid or negative monetary amounts where inappropriate.
- Validating required fields.
- Checking date formats.
- Preventing invalid repayment amounts.
- Handling missing records.
- Returning meaningful HTTP error responses.

The frontend will display understandable error messages to users.

## 10. Testing Architecture

Testing will be performed throughout development.

### Backend Testing

Pytest will be used to test:

- Income management.
- Expense management.
- Budget calculations.
- Daily spending recommendations.
- Debt management.
- Repayment calculations.
- API endpoints.
- Input validation.

### Frontend Testing

Frontend testing will cover:

- Component behavior.
- Form validation.
- API communication.
- Navigation.
- Dashboard updates.
- Accessibility and usability.

### Integration Testing

Integration testing will verify that the frontend, backend, and database work together correctly.

## 11. Deployment Considerations

During development:

- The React frontend will run locally.
- The FastAPI backend will run locally.
- SQLite will store application data locally.

The architecture should allow future deployment to a web hosting environment.

Before public deployment, appropriate authentication, authorization, HTTPS, database backup, and production configuration must be implemented.

## 12. Future Scalability

The architecture should support future improvements, including:

- Migration from SQLite to PostgreSQL.
- Advanced financial reports and visualizations.
- AI-powered financial assistance.
- Voice-based interaction.
- Savings goals.
- Additional financial planning features.
- Optional cloud synchronization.

The modular structure will allow new features to be added without unnecessarily changing existing components.

## 13. Architectural Summary

SpendWise will use a three-layer architecture with React as the presentation layer, FastAPI as the application layer, and SQLite as the initial data layer.

The backend will follow a modular monolithic structure, separating API routes, database models, validation schemas, services, and configuration.

This architecture provides a practical foundation for developing a maintainable, secure, and extensible personal finance management application.