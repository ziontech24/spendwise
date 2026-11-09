import {
  LayoutDashboard,
  ArrowLeftRight,
  Wallet,
  Users,
  CalendarDays,
  ChartNoAxesCombined,
  Settings,
  Bell,
  Plus,
  ArrowUpRight,
  ArrowDownRight,
  Sparkles,
  Menu,
} from "lucide-react";
import { NavLink } from "react-router-dom";
import "./Dashboard.css";

// Temporary sample financial data
const financialData = [
  {
    title: "Total Income",
    amount: "15,000",
    change: "+12.5%",
    description: "Compared to last month",
    icon: ArrowDownRight,
    type: "income",
  },
  {
    title: "Total Expenses",
    amount: "6,500",
    change: "+4.2%",
    description: "Compared to last month",
    icon: ArrowUpRight,
    type: "expense",
  },
  {
    title: "Available Balance",
    amount: "8,500",
    change: "Your current balance",
    description: "Based on recorded transactions",
    icon: Wallet,
    type: "balance",
  },
  {
    title: "Budget Remaining",
    amount: "3,500",
    change: "35% remaining",
    description: "Of your monthly budget",
    icon: ChartNoAxesCombined,
    type: "budget",
  },
];

const navigationItems = [
  { label: "Dashboard", icon: LayoutDashboard, path: "/dashboard" },
  { label: "Transactions", icon: ArrowLeftRight, path: "/transactions" },
  { label: "Budgets", icon: Wallet, path: "/budgets" },
  { label: "People & Money", icon: Users, path: "/people-money" },
  { label: "Planned Expenses", icon: CalendarDays, path: "/planned-expenses" },
  { label: "Reports", icon: ChartNoAxesCombined, path: "/reports" },
];

function getGreeting() {
  const hour = new Date().getHours();

  if (hour < 12) return "Good morning";
  if (hour < 18) return "Good afternoon";

  return "Good evening";
}

// Our original SpendWise mascot illustration
function SpendWiseMascot() {
  return (
    <svg
      viewBox="0 0 220 190"
      role="img"
      aria-label="A friendly illustrated green character waving"
      className="mascot"
    >
      {/* Decorative elements */}
      <path
        d="M34 45 Q20 30 35 22"
        stroke="#116B62"
        strokeWidth="3"
        fill="none"
        strokeLinecap="round"
      />

      <path
        d="M184 40 Q200 25 190 15"
        stroke="#116B62"
        strokeWidth="3"
        fill="none"
        strokeLinecap="round"
      />

      <circle cx="30" cy="75" r="5" fill="#F2A65A" />
      <circle cx="191" cy="85" r="5" fill="#F2A65A" />

      {/* Body */}
      <path
        d="M65 102 Q55 160 83 171 Q110 184 137 171 Q165 155 151 102Z"
        fill="#116B62"
      />

      {/* Face */}
      <ellipse cx="108" cy="76" rx="57" ry="52" fill="#DDF3EC" />

      {/* Eyes */}
      <ellipse cx="88" cy="72" rx="5" ry="7" fill="#202C2A" />
      <ellipse cx="128" cy="72" rx="5" ry="7" fill="#202C2A" />

      {/* Smile */}
      <path
        d="M94 91 Q108 105 123 91"
        stroke="#202C2A"
        strokeWidth="3"
        fill="none"
        strokeLinecap="round"
      />

      {/* Cheeks */}
      <ellipse cx="75" cy="88" rx="9" ry="5" fill="#F2A65A" opacity=".6" />
      <ellipse cx="142" cy="88" rx="9" ry="5" fill="#F2A65A" opacity=".6" />

      {/* Waving arm */}
      <path
        d="M148 119 Q175 100 174 66"
        stroke="#116B62"
        strokeWidth="13"
        fill="none"
        strokeLinecap="round"
      />

      {/* Hand */}
      <circle cx="175" cy="61" r="10" fill="#DDF3EC" />

      {/* Feet */}
      <ellipse cx="87" cy="172" rx="18" ry="7" fill="#0B4943" />
      <ellipse cx="135" cy="172" rx="18" ry="7" fill="#0B4943" />

      {/* Small leaf */}
      <path
        d="M105 27 Q115 5 137 17 Q130 35 105 27Z"
        fill="#75B99B"
      />
    </svg>
  );
}

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="brand">
        <div className="brand-icon">
          <Wallet size={23} />
        </div>

        <span>SpendWise</span>
      </div>

      <p className="nav-heading">MENU</p>

      <nav className="navigation">

  {navigationItems.map((item) => {

    const Icon = item.icon;

    return (

      <NavLink
        to={item.path}
        key={item.label}
        className={({ isActive }) =>
          `nav-item ${isActive ? "active" : ""}`
        }
      >

        <Icon size={19} />

        <span>{item.label}</span>

      </NavLink>

    );

  })}

</nav>

      <div className="sidebar-bottom">
        <a href="#settings" className="nav-item">
          <Settings size={19} />
          <span>Settings</span>
        </a>

        <div className="sidebar-note">
          <Sparkles size={19} />
          <p>Your journey to financial peace starts here.</p>
        </div>
      </div>
    </aside>
  );
}

function SummaryCard({ item }) {
  const Icon = item.icon;

  return (
    <article className={`summary-card ${item.type}`}>
      <div className="summary-top">
        <span>{item.title}</span>

        <div className="summary-icon">
          <Icon size={20} />
        </div>
      </div>

      <h2>ETB {item.amount}</h2>

      <p className="summary-change">{item.change}</p>
      <p className="summary-description">{item.description}</p>
    </article>
  );
}

function Dashboard() {
  const today = new Date();
  const username = "Zion";

  return (
    <div className="dashboard-layout" id="dashboard">
      <Sidebar />

      <main className="dashboard-main">
        <header className="topbar">
          <button className="mobile-menu" aria-label="Open navigation">
            <Menu size={22} />
          </button>

          <div className="breadcrumb">
            My Space <span>/</span> Dashboard
          </div>

          <div className="topbar-actions">
            <button className="notification-button" aria-label="Notifications">
              <Bell size={20} />
              <span className="notification-dot"></span>
            </button>

            <div className="profile-avatar">S</div>
          </div>
        </header>

        <div className="dashboard-content">
          {/* Welcome section */}
          <section className="welcome-section">
            <div className="welcome-text">
              <p className="welcome-date">
                {today.toLocaleDateString("en-US", {
                  weekday: "long",
                  month: "long",
                  day: "numeric",
                  year: "numeric",
                })}
              </p>

              <h1>{getGreeting()}, {username}!</h1>

              <p className="welcome-message">
               Let's make today a good day for your money.
              </p>
              <button className="primary-button">
                <Plus size={18} />
                Add transaction
              </button>
            </div>

            <div className="welcome-illustration">
              <SpendWiseMascot />
              <div className="mascot-message">
                <Sparkles size={15} />
                Small steps make a big difference!
              </div>
            </div>
          </section>

          {/* Financial summary */}
          <section className="section">
            <div className="section-heading">
              <div>
                <h2>Your financial overview</h2>
                <p>Here's how your money is doing this month.</p>
              </div>

              <span className="period-label">November 2026</span>
            </div>

            <div className="summary-grid">
              {financialData.map((item) => (
                <SummaryCard key={item.title} item={item} />
              ))}
            </div>
          </section>

          {/* Budget guidance */}
          <section className="guidance-section">
            <div className="guidance-icon">
              <Sparkles size={24} />
            </div>

            <div className="guidance-content">
              <h3>A little spending guidance</h3>

              <p>
                You have ETB 3,500 remaining in your monthly budget.
                Keep an eye on your spending and remember to leave
                room for upcoming expenses.
              </p>

              <div className="budget-progress">
                <div className="progress-track">
                  <div className="progress-fill"></div>
                </div>

                <span>65% of budget used</span>
              </div>
            </div>
          </section>

          {/* Lower dashboard sections */}
          <section className="bottom-grid">
            <article className="dashboard-panel">
              <div className="panel-heading">
                <div>
                  <h2>Recent transactions</h2>
                  <p>Your latest money activities.</p>
                </div>

                <button className="text-button">View all</button>
              </div>

              <div className="empty-state">
                <ArrowLeftRight size={28} />

                <h3>Your transactions will appear here</h3>

                <p>
                  Once you record your income and expenses,
                  you can track them here.
                </p>
              </div>
            </article>

            <article className="dashboard-panel">
              <div className="panel-heading">
                <div>
                  <h2>Upcoming expenses</h2>
                  <p>Things you are planning for.</p>
                </div>

                <CalendarDays size={21} />
              </div>

              <div className="empty-state">
                <CalendarDays size={28} />

                <h3>Nothing planned yet</h3>

                <p>
                  Add a planned expense to prepare for
                  upcoming payments.
                </p>
              </div>
            </article>
          </section>

          <footer className="dashboard-footer">
            Made for your financial peace of mind. 💚
          </footer>
        </div>
      </main>
    </div>
  );
}

export { Sidebar };
export default Dashboard;