from datetime import datetime
from typing import TYPE_CHECKING, Optional, List

from modules.base import BaseService
from modules.transactions.domain.entities import TransactionEntity

if TYPE_CHECKING:
    from modules.transactions.domain.interfaces import ITransactionRepository


class TransactionService(BaseService[TransactionEntity]):
    def __init__(self, repo: "ITransactionRepository",):
        super(TransactionService, self).__init__(repo)

    async def get_summary(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> tuple[float, float]:
        total_income, total_expense = await self.repo.get_summary(start_date, end_date)
        return total_income, total_expense

    async def get_expenses_by_category(
        self,
        start_date: datetime,
        end_date: datetime,
    ) -> List[tuple[str, float]]:
        expenses = await self.repo.get_expenses_by_category(start_date, end_date)
        return expenses
