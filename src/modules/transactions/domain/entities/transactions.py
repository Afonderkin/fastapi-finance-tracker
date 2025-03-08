from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from modules.base import BaseEntity
from modules.transactions.domain.value_objects import Description


@dataclass
class TransactionType(Enum):
    INCOME: str = "Доход"
    EXPENSE: str = "Расход"


@dataclass
class TransactionEntity(BaseEntity[int]):
    amount: float
    transaction_type: TransactionType
    date: datetime
    category_id: int
    description: Optional[Description] = None

    def __post_init__(self):
        if self.transaction_type == TransactionType.EXPENSE:
            self.amount = -self.amount

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: 'TransactionEntity') -> bool:
        return self.id == other.id

    def __str__(self) -> str:
        return (f"TransactionEntity(id={self.id}, amount={self.amount}, description={self.description},"
                f" transaction_type={self.transaction_type}), date={self.date}, category_id={self.category_id}")
