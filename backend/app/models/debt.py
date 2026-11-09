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


class Debt(Base):
    __tablename__ = "debts"

    __table_args__ = (
        CheckConstraint(
            "direction IN ('borrowed', 'lent')",
            name="check_debt_direction",
        ),
        CheckConstraint(
            "amount_minor > 0",
            name="check_debt_amount",
        ),
        CheckConstraint(
            "status IN ('pending', 'partially_paid', 'settled')",
            name="check_debt_status",
        ),
        Index("idx_debts_user", "user_id"),
        Index("idx_debts_due_date", "due_date"),
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

    person_name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    direction: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    amount_minor: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    date_recorded: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    due_date: Mapped[Date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        server_default=text("'pending'"),
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    user = relationship("User", back_populates="debts")

    repayments = relationship(
        "Repayment",
        back_populates="debt",
        cascade="all, delete-orphan",
    )