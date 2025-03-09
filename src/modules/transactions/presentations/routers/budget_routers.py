from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, status, Depends, Query, HTTPException

from core.config import settings
from modules.transactions.domain.services import TransactionService, BudgetService
from modules.transactions.presentations.dependencies import get_transaction_service, get_budget_service
from modules.transactions.presentations.schemas import SummaryResponse, ExpensesByCategoryResponse, BudgetResponse, \
    BudgetCreate

router = APIRouter(
    prefix=settings.api.v1.budgets_prefix,
    tags=["Бюджеты"],
)


@router.post(
    path="",
    response_model=BudgetResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Установка лимита бюджета",
    description="Устанавливает лимит бюджета для категории на определённый период.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    },
)
async def set_budget_limit(
    budget_service: Annotated[BudgetService, Depends(get_budget_service)],
    budget_data: BudgetCreate,
) -> BudgetResponse:
    budget = await budget_service.create(
        category_id=budget_data.category_id,
        limit=budget_data.limit,
        period_start=budget_data.period_start,
        period_end=budget_data.period_end,
    )

    actual_expenses = await budget_service.repo.get_actual_expenses(
        category_id=budget_data.category_id,
        period_start=budget_data.period_start,
        period_end=budget_data.period_end,
    )

    return BudgetResponse(
        id=budget.id,
        category_id=budget.category_id,
        limit=budget.limit,
        period_start=budget.period_start,
        period_end=budget.period_end,
        actual_expenses=actual_expenses,
        remaining_budget=budget.limit - actual_expenses,
    )


@router.get(
    path="/{category_id}",
    response_model=BudgetResponse,
    summary="Получение информации о бюджете",
    description="Возвращает информацию о бюджете для категории за указанный период.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Бюджет для категории не найден",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    },
)
async def get_budget(
    budget_service: Annotated[BudgetService, Depends(get_budget_service)],
    category_id: int,
    period_start: datetime = Query(..., description="Начало периода", example="2025-03-01T00:00:00"),
    period_end: datetime = Query(..., description="Конец периода", example="2025-04-01T00:00:00"),
) -> BudgetResponse:
    budget = await budget_service.repo.get_budget_for_category(
        category_id=category_id,
        period_start=period_start,
        period_end=period_end,
    )

    if not budget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Бюджет для категории {category_id} не найден",
        )

    actual_expenses = await budget_service.repo.get_actual_expenses(
        category_id=category_id,
        period_start=period_start,
        period_end=period_end,
    )

    return BudgetResponse(
        id=budget.id,
        category_id=budget.category_id,
        limit=budget.limit,
        period_start=budget.period_start,
        period_end=budget.period_end,
        actual_expenses=actual_expenses,
        remaining_budget=budget.limit - actual_expenses,
    )