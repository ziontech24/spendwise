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


class PlannedExpense(Base):
    __tablename__ = "planned_expenses"

    __table_args__ = (
        CheckConstraint(
            "amount_minor > 0",
            name="check_planned_expense_amount",
        ),
        CheckConstraint(
            "status IN ('planned', 'paid', 'cancelled')",
            name="check_planned_expense_status",
        ),
        Index("idx_planned_user", "user_id"),
        Index("idx_planned_date", "planned_date"),
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

    title: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    amount_minor: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    planned_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        server_default=text("'planned'"),
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    user = relationship("User", back_populates="planned_expenses")
    category = relationship("Category", back_populates="planned_expenses")