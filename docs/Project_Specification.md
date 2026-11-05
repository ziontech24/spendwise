# SpendWise — Project Specification

## 1. Project Overview

**SpendWise** is a personalized financial management web application designed to help individuals understand, organize, and manage their personal finances.

Unlike a traditional expense tracker, SpendWise aims to act as a personal finance companion. It helps users monitor their income and expenses, manage budgets, track money they owe or are owed, and make more informed daily spending decisions.

The application provides a personalized dashboard with friendly greetings, financial summaries, spending recommendations, and useful reminders.

**Project slogan:** Your money. Your budget. Your peace of mind.

## 2. Problem Statement

Many individuals struggle to manage their personal finances because they lack a simple and organized way to:

- Track their income and daily expenses.
- Understand where their money goes.
- Maintain monthly and category-based budgets.
- Decide how much they can reasonably spend each day.
- Remember money borrowed from or lent to other people.
- Keep track of repayments and outstanding balances.
- Monitor their financial progress.

Traditional expense trackers often focus primarily on recording transactions. SpendWise aims to provide a more interactive and personalized experience that helps users understand their financial situation and make better spending decisions.

## 3. Project Objectives

The main objectives of SpendWise are to:

1. Provide an organized system for recording income and expenses.
2. Help users create and monitor personal budgets.
3. Calculate recommended daily spending amounts based on available financial information.
4. Track money borrowed from and lent to other people.
5. Monitor repayments and outstanding balances.
6. Provide personalized financial summaries and reminders.
7. Make personal finance management simple, understandable, and accessible.
8. Protect users' financial information through privacy-conscious design.

## 4. Target Users

SpendWise is designed for individuals who want to improve their personal financial management.

Potential users include:

- University students managing limited monthly budgets.
- Employees tracking their salaries and expenses.
- Individuals who want to develop better spending habits.
- People who frequently borrow or lend money.
- Anyone looking for a simple personal finance management tool.

## 5. Core Features — Version 1

### 5.1 Personalized Dashboard

The dashboard will provide an overview of the user's financial situation.

Features:
- Personalized greetings based on the time of day.
- Friendly and varied motivational messages.
- Total income and expenses.
- Current budget information.
- Remaining budget.
- Recommended daily spending amount.
- Important financial reminders.

The dashboard should only display information supported by the user's recorded financial data.

### 5.2 Income Management

Users can record their income.

Each income record should include:
- Amount.
- Income source.
- Date received.
- Description (optional).

Users should be able to view, update, and delete income records.

### 5.3 Expense Management

Users can record and manage their daily expenses.

Each expense record should include:
- Amount.
- Expense category.
- Date.
- Description (optional).

Example categories:
- Food.
- Transportation.
- Education.
- Housing.
- Shopping.
- Entertainment.
- Healthcare.
- Other.

Users should be able to view, update, and delete expenses.

### 5.4 Budget Management

Users can establish monthly and category-based budgets.

Features:
- Set a total monthly budget.
- Set spending limits for individual categories.
- Monitor spending against each budget.
- Display remaining budget.
- Provide notifications when spending approaches or exceeds a budget.

### 5.5 Daily Spending Recommendation

SpendWise will calculate a recommended daily spending amount.

The calculation may consider:
- Remaining budget.
- Number of days left in the budget period.
- Planned upcoming expenses.
- Financial commitments recorded by the user.

The recommendation is intended as guidance, not a restriction.

SpendWise should explain how the recommendation was calculated so users can understand the result.

### 5.6 People & Money

This feature helps users manage money they borrow from or lend to other people.

It has two main sections:

**A. Money I Owe**

Users can record money borrowed from friends, family members, or other people.

Information includes:
- Person's name.
- Amount borrowed.
- Date borrowed.
- Expected repayment date.
- Description or reason.
- Amount repaid.
- Remaining balance.
- Repayment status.

**B. Money Owed to Me**

Users can record money lent to other people.

Information includes:
- Person's name.
- Amount lent.
- Date lent.
- Expected repayment date.
- Description.
- Amount received back.
- Remaining balance.
- Repayment status.

Users should be able to record partial repayments and view outstanding balances.

Money owed to the user must not automatically be treated as available cash until it is actually received.

### 5.7 Repayment Tracking

Users should be able to record repayments for borrowed or lent money.

Features:
- Record full or partial repayments.
- Automatically update outstanding balances.
- Display repayment history.
- Identify fully settled and outstanding transactions.
- Provide reminders for approaching due dates.

### 5.8 Planned Expenses

Users can record expenses they expect to make in the future.

Examples:
- Monthly rent.
- Tuition fees.
- Upcoming purchases.
- Utility bills.

Planned expenses can help improve daily spending recommendations and financial planning.

### 5.9 Interactive Financial Questions

SpendWise will provide a simple question-and-answer interface for common financial questions.

Initial questions will use predefined calculations and recorded financial data.

Examples:
- How much money have I spent this month?
- How much can I spend today?
- How much money do I owe?
- How much money do other people owe me?
- How much of my monthly budget remains?
- Which category has the highest spending?

This feature will initially use rule-based logic rather than a complex AI model.

### 5.10 Reminders and Notifications

SpendWise will provide useful reminders for:

- Upcoming repayment dates.
- Outstanding borrowed or lent money.
- Approaching budget limits.
- Planned expenses.

Notifications should be informative and friendly rather than overwhelming.

## 6. Future Features

The following features are outside the initial version but may be introduced in future releases.

- Savings goals and progress tracking.
- Advanced financial reports and interactive charts.
- AI-powered financial assistant.
- Voice-based interaction.
- More advanced financial recommendations.
- Exporting financial reports.
- Optional cloud synchronization.
- Additional personalization options.

These features will be considered after the core application is stable.

## 7. Functional Requirements

The application must allow users to:

1. Access their personalized dashboard.
2. Record, view, update, and delete income.
3. Record, view, update, and delete expenses.
4. Create and manage budgets.
5. View remaining budgets.
6. Receive daily spending recommendations.
7. Record borrowed and lent money.
8. Record full and partial repayments.
9. View outstanding balances.
10. Create and manage planned expenses.
11. View financial summaries.
12. Ask predefined financial questions.
13. Receive relevant reminders.

## 8. Non-Functional Requirements

### 8.1 Usability

The interface should be simple, intuitive, and easy to navigate.

### 8.2 Performance

The application should respond efficiently to user actions and financial calculations.

### 8.3 Security

Financial information must be protected. Sensitive data should not be exposed through unnecessary logs, insecure endpoints, or careless data handling.

### 8.4 Privacy

SpendWise should follow a privacy-conscious approach by collecting and retaining only the information necessary for its functionality.

### 8.5 Accessibility

The interface should support:
- Keyboard navigation.
- Clear labels and instructions.
- Readable text and sufficient contrast.
- Screen-reader-friendly interface elements.

### 8.6 Maintainability

The application should use a modular structure so that features can be developed, tested, and maintained independently.

### 8.7 Reliability

Financial calculations should be accurate and consistent. The system should handle invalid inputs and missing information appropriately.

## 9. Proposed Technology Stack

| Component | Technology |
|---|---|
| Frontend | React.js |
| Programming Language | JavaScript |
| Styling | CSS |
| Backend | Python |
| Backend Framework | FastAPI |
| Database | SQLite initially |
| API Communication | REST API |
| Version Control | Git and GitHub |
| Development Environment | Visual Studio Code |

The architecture should allow the database and other technologies to be upgraded in the future if necessary.

## 10. Project Scope

### Included in Version 1

- Personalized dashboard.
- Income management.
- Expense management.
- Monthly and category-based budgets.
- Daily spending recommendations.
- People & Money management.
- Repayment tracking.
- Planned expenses.
- Rule-based financial questions.
- Basic reminders.

### Not Included in Version 1

- Advanced AI financial assistant.
- Voice-based financial interaction.
- Advanced investment management.
- Bank account integration.
- Automatic transaction synchronization.
- Complex financial forecasting.

## 11. Expected Outcome

The expected outcome is a functional, user-friendly personal finance web application that helps individuals understand their financial activities and manage their money more effectively.

SpendWise should provide more than a place to record transactions. It should help users understand their financial position, plan their spending, keep track of financial commitments, and make informed everyday decisions.

## 12. Project Development Approach

SpendWise will be developed incrementally.

The development process will include:

1. Project planning and documentation.
2. System architecture and database design.
3. Backend foundation and API development.
4. Frontend foundation and interface development.
5. Financial management features.
6. Budget and spending recommendation system.
7. People & Money and repayment management.
8. Dashboard integration.
9. Testing, debugging, and improvements.
10. Final documentation and deployment preparation.

Git and GitHub will be used for version control, with separate branches for feature development and integration.