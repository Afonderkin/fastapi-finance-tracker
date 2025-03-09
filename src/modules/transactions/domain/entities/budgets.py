from dataclasses import dataclass
from datetime import datetime

from modules.base import BaseEntity


@dataclass
class BudgetEntity(BaseEntity[int]):
    category_id: int
    limit: float
    period_start: datetime
    period_end: datetime

    def __post_init__(self):
        self._validate_limit()
        self._validate_period()

    def _validate_period(self) -> bool:
        return self.period_start < self.period_end

    def _validate_limit(self) -> bool:
        return self.limit >= 0

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: 'BudgetEntity') -> bool:
        return self.id == other.id

    def __str__(self):
        return (f"BudgetEntity(id={self.id}, limit={self.limit},"
                f" period_start={self.period_start}, period_end={self.period_end}")
