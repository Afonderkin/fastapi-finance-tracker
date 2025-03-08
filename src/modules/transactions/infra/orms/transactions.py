from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.base import BaseModel
from modules.transactions.domain.entities import TransactionType, TransactionEntity
from modules.transactions.domain.value_objects import Description

if TYPE_CHECKING:
    from modules.categories.infra.orms import Category


class Transaction(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    transaction_type: Mapped[TransactionType] = mapped_column(Enum(TransactionType), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    category_id: Mapped[int] =  mapped_column(ForeignKey("categories.id"), nullable=False)

    category: Mapped["Category"] = relationship(back_populates="transactions")

    def to_entity(self):
        return TransactionEntity(
            id=self.id,
            amount=self.amount,
            description=Description(self.description),
            transaction_type=self.transaction_type,
            date=self.date,
            category_id=self.category_id,
        )

    def __str__(self):
        return (f"Transaction(id={self.id}, amount={self.amount}, description={self.description},"
                f" transaction_type={self.transaction_type} date={self.date}, category_id={self.category_id})")

    def __repr__(self):
        return (f"Transaction(id={self.id}, amount={self.amount}, description={self.description},"
                f" transaction_type={self.transaction_type} date={self.date}, category_id={self.category_id})")
