from datetime import datetime
from typing import TYPE_CHECKING, Optional, List

from modules.base import BaseService
from modules.transactions.domain.entities import TransactionEntity
from modules.transactions.domain.services import BudgetService

if TYPE_CHECKING:
    from modules.transactions.domain.interfaces import ITransactionRepository


class TransactionService(BaseService[TransactionEntity]):
    def __init__(
        self,
        repo: "ITransactionRepository",
        budget_service: BudgetService,
    ):
        super(TransactionService, self).__init__(repo)
        self.budget_service = budget_service

    async def create(self, **data) -> "TransactionEntity":
        period_start = datetime.now().replace(day=1)
        period_end = datetime.now().replace(day=31)

        await self.budget_service.check_budget_limit(
            category_id=data["category_id"],
            amount=data["amount"],
            period_start=period_start,
            period_end=period_end,
        )

        transaction = await self.repo.save(**data)
        return transaction.to_entity()

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
