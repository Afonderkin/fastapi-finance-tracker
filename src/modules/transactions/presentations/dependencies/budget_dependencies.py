from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper
from modules.transactions.domain.interfaces import IBudgetRepository
from modules.transactions.domain.services import BudgetService
from modules.transactions.infra.repositories import InMemoryBudgetRepository


def get_budget_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> IBudgetRepository:
    return InMemoryBudgetRepository(session)


def get_budget_service(
    budget_repository: Annotated[IBudgetRepository, Depends(get_budget_repository)]
) -> BudgetService:
    return BudgetService(budget_repository)
