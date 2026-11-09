from sqlalchemy import (
    Integer,
    Text,
    Date,
    DateTime,
    ForeignKey,
    CheckConstraint,
    text,
    Index,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Budget(Base):
    __tablename__ = "budgets"

    __table_args__ = (
        CheckConstraint(
            "amount_minor > 0",
            name="check_budget_amount",
        ),
        CheckConstraint(
            "period = 'monthly'",
            name="check_budget_period",
        ),
        CheckConstraint(
            "start_date <= end_date",
            name="check_budget_dates",
        ),
        Index("idx_budgets_user", "user_id"),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    category_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("categories.id"),
        nullable=True,
    )

    amount_minor: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    period: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    start_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    user = relationship("User", back_populates="budgets")
    category = relationship("Category", back_populates="budgets")