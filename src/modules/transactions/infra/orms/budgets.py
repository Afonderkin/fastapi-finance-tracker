from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.base import BaseModel
from modules.transactions.domain.entities import BudgetEntity

if TYPE_CHECKING:
    from modules.categories.infra.orms import Category


class Budget(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    limit: Mapped[float] = mapped_column(nullable=False)
    period_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    period_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    category: Mapped["Category"] = relationship(back_populates="budgets")

    def to_entity(self):
        return BudgetEntity(
            id=self.id,
            category_id=self.category_id,
            limit=self.limit,
            period_start=self.period_start,
            period_end=self.period_end,
        )

    def __str__(self):
        return (f"Budget(id={self.id}, category_id={self.category_id},"
                f"limit={self.limit}, period_start={self.period_start},"
                f"period_end={self.period_end})")

    def __repr__(self):
        return (f"Budget(id={self.id}, category_id={self.category_id},"
                f"limit={self.limit}, period_start={self.period_start},"
                f"period_end={self.period_end})")
