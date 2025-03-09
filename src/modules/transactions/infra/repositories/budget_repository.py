from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import select, func

from modules.base import InMemoryBaseRepository
from modules.transactions.domain.entities import TransactionType
from modules.transactions.infra.orms import Budget, Transaction

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class InMemoryBudgetRepository(InMemoryBaseRepository[Budget]):
    model: Budget = Budget

    def __init__(self, session: "AsyncSession") -> None:
        super(InMemoryBudgetRepository, self).__init__(session)

    async def get_budget_for_category(
        self,
        category_id: int,
        period_start: datetime,
        period_end: datetime,
    ) -> Optional[Budget]:
        stmt = select(self.model).where(
            self.model.category_id == category_id,
            self.model.period_start <= period_end,
            self.model.period_end >= period_start,
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_actual_expenses(
        self,
        category_id: int,
        period_start: datetime,
        period_end: datetime,
    ) -> float:
        stmt = select(func.sum(Transaction.amount)).where(
            Transaction.category_id == category_id,
            Transaction.transaction_type == TransactionType.EXPENSE,
            Transaction.date >= period_start,
            Transaction.date <= period_end,
        )
        result = await self.session.execute(stmt)
        return result.scalar() or 0.0
