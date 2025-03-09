from datetime import datetime
from typing import TYPE_CHECKING, Optional, List

from modules.base import BaseService
from modules.transactions.domain.entities import BudgetEntity
from modules.transactions.exceptions import BudgetLimitExceededException

if TYPE_CHECKING:
    from modules.transactions.domain.interfaces import IBudgetRepository


class BudgetService(BaseService[BudgetEntity]):
    def __init__(self, repo: "IBudgetRepository",):
        super(BudgetService, self).__init__(repo)

    async def check_budget_limit(
        self,
        category_id: int,
        amount: float,
        period_start: datetime,
        period_end: datetime
    ) -> bool:
        budget = await self.repo.get_budget_for_category(category_id, period_start, period_end)
        if not budget:
            return True

        actual_expenses = await self.repo.get_actual_expenses(category_id, period_start, period_end)
        if actual_expenses + amount > budget.limit:
            raise BudgetLimitExceededException(
                f"Превышен лимит бюджета для категории {category_id}. Лимит: {budget.limit},"
                f" Фактические расходы: {actual_expenses}"
            )
        return True
