import {
  ArrowLeftRight,
  ArrowDownRight,
  ArrowUpRight,
  Wallet,
  Plus,
  Search,
  Filter,
  CalendarDays,
  MoreHorizontal,
  TrendingUp,
  TrendingDown,
} from "lucide-react";

import { NavLink } from "react-router-dom";

import { Sidebar } from "./Dashboard";

import "./Dashboard.css";
import "./Transactions.css";

// Temporary transaction data
const transactions = [
  {
    id: 1,
    title: "Monthly Salary",
    category: "Salary",
    date: "Nov 01, 2026",
    amount: 15000,
    type: "income",
  },
  {
    id: 2,
    title: "Grocery Shopping",
    category: "Food",
    date: "Nov 03, 2026",
    amount: 1200,
    type: "expense",
  },
  {
    id: 3,
    title: "Transportation",
    category: "Transport",
    date: "Nov 04, 2026",
    amount: 350,
    type: "expense",
  },
  {
    id: 4,
    title: "Freelance Project",
    category: "Freelance",
    date: "Nov 05, 2026",
    amount: 2500,
    type: "income",
  },
  {
    id: 5,
    title: "Internet Payment",
    category: "Utilities",
    date: "Nov 05, 2026",
    amount: 800,
    type: "expense",
  },
  {
    id: 6,
    title: "Lunch",
    category: "Food",
    date: "Nov 06, 2026",
    amount: 250,
    type: "expense",
  },
];

// Format money
function formatMoney(amount) {
  return new Intl.NumberFormat("en-US").format(amount);
}

// Transaction summary card
function TransactionSummaryCard({
  title,
  amount,
  description,
  icon: Icon,
  type,
}) {
  return (
    <article className={`transaction-summary-card ${type}`}>
      <div className="transaction-summary-top">
        <span>{title}</span>

        <div className="transaction-summary-icon">
          <Icon size={20} />
        </div>
      </div>

      <h2>ETB {formatMoney(amount)}</h2>

      <p>{description}</p>
    </article>
  );
}

// Main Transactions page
function Transactions() {
  const totalIncome = transactions
    .filter((transaction) => transaction.type === "income")
    .reduce((total, transaction) => total + transaction.amount, 0);

  const totalExpenses = transactions
    .filter((transaction) => transaction.type === "expense")
    .reduce((total, transaction) => total + transaction.amount, 0);

  const netAmount = totalIncome - totalExpenses;

  return (
    <div className="dashboard-layout">
      <Sidebar />

      <main className="dashboard-main">
        {/* Top navigation */}
<header className="topbar">
  <div className="breadcrumb">
    <NavLink to="/dashboard" className="dashboard-link">
      Dashboard
    </NavLink>

    <span>/</span>

    Transactions
  </div>

  <div className="topbar-actions">
    <div className="profile-avatar">Z</div>
  </div>
</header>

        <div className="dashboard-content transactions-content">
          {/* Page heading */}
          <section className="transactions-heading">
            <div>
              <span className="transactions-eyebrow">
                YOUR MONEY ACTIVITY
              </span>

              <h1>Transactions</h1>

              <p>
                Every little detail matters. Here's where your money
                comes and goes.
              </p>
            </div>

            <button className="primary-button">
              <Plus size={18} />
              Add transaction
            </button>
          </section>

          {/* Compact financial summary */}
<section className="transaction-overview">
  <div className="overview-item">
    <span className="overview-label">Income</span>
    <h3 className="income-text">
      + ETB {formatMoney(totalIncome)}
    </h3>
  </div>

  <div className="overview-divider"></div>

  <div className="overview-item">
    <span className="overview-label">Expenses</span>
    <h3 className="expense-text">
      - ETB {formatMoney(totalExpenses)}
    </h3>
  </div>

  <div className="overview-divider"></div>

  <div className="overview-item">
    <span className="overview-label">Difference</span>
    <h3 className={netAmount >= 0 ? "income-text" : "expense-text"}>
      {netAmount < 0 ? "-" : "+"} ETB {formatMoney(Math.abs(netAmount))}
    </h3>
  </div>
</section>
          {/* Transaction history */}
          <section className="transactions-panel">
            <div className="transactions-panel-heading">
              <div>
                <h2>Transaction history</h2>

                <p>
                  Your income and expenses, all in one place.
                </p>
              </div>

              <span className="transaction-count">
                {transactions.length} transactions
              </span>
            </div>

            {/* Search and filters */}
            <div className="transaction-toolbar">
              <div className="transaction-search">
                <Search size={18} />

                <input
                  type="text"
                  placeholder="Search transactions..."
                  aria-label="Search transactions"
                />
              </div>

              <div className="transaction-filters">
                <button className="transaction-filter active">
                  All
                </button>

                <button className="transaction-filter">
                  Income
                </button>

                <button className="transaction-filter">
                  Expenses
                </button>
              </div>

              <button
                className="transaction-filter-button"
                aria-label="More filters"
              >
                <Filter size={18} />
                Filter
              </button>
            </div>

            {/* Table */}
            <div className="transaction-table-wrapper">
              <table className="transaction-table">
                <thead>
                  <tr>
                    <th>TRANSACTION</th>
                    <th>CATEGORY</th>
                    <th>DATE</th>
                    <th>TYPE</th>
                    <th>AMOUNT</th>
                    <th></th>
                  </tr>
                </thead>

                <tbody>
                  {transactions.map((transaction) => {
                    const isIncome = transaction.type === "income";

                    return (
                      <tr key={transaction.id}>
                        <td>
                          <div className="transaction-name-cell">
                            <div
                              className={`transaction-type-icon ${
                                isIncome ? "income" : "expense"
                              }`}
                            >
                              {isIncome ? (
                                <ArrowDownRight size={19} />
                              ) : (
                                <ArrowUpRight size={19} />
                              )}
                            </div>

                            <div>
                              <span className="transaction-title">
                                {transaction.title}
                              </span>

                              <span className="transaction-category-mobile">
                                {transaction.category}
                              </span>
                            </div>
                          </div>
                        </td>

                        <td>
                          <span className="category-badge">
                            {transaction.category}
                          </span>
                        </td>

                        <td>
                          <div className="transaction-date">
                            <CalendarDays size={15} />

                            {transaction.date}
                          </div>
                        </td>

                        <td>
                          <span
                            className={`transaction-type-badge ${
                              isIncome ? "income" : "expense"
                            }`}
                          >
                            {isIncome ? "Income" : "Expense"}
                          </span>
                        </td>

                        <td>
                          <span
                            className={`transaction-amount ${
                              isIncome ? "income" : "expense"
                            }`}
                          >
                            {isIncome ? "+" : "-"} ETB{" "}
                            {formatMoney(transaction.amount)}
                          </span>
                        </td>

                        <td>
                          <button
                            className="transaction-more-button"
                            aria-label={`More options for ${transaction.title}`}
                          >
                            <MoreHorizontal size={19} />
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>

            {/* Footer */}
            <div className="transactions-panel-footer">
              <span>
                Showing {transactions.length} transactions
              </span>

              <button className="text-button">
                View all transactions
              </button>
            </div>
          </section>

          {/* Friendly note */}
          <div className="transactions-note">
            <div className="transactions-note-icon">
              <ArrowLeftRight size={20} />
            </div>

            <div>
              <h3>Your money, your story.</h3>

              <p>
                Every transaction helps you understand your
                financial habits and make better decisions.
              </p>
            </div>
          </div>

          <footer className="dashboard-footer">
            Made for your financial peace of mind. 💚
          </footer>
        </div>
      </main>
    </div>
  );
}

export default Transactions;