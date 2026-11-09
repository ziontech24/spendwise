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


class Repayment(Base):
    __tablename__ = "repayments"

    __table_args__ = (
        CheckConstraint(
            "amount_minor > 0",
            name="check_repayment_amount",
        ),
        Index("idx_repayments_debt", "debt_id"),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,

    )

    debt_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("debts.id", ondelete="CASCADE"),
        nullable=False,
    )

    amount_minor: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    repayment_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    debt = relationship("Debt", back_populates="repayments")