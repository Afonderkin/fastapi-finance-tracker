from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, status, Depends, Query

from core.config import settings
from modules.transactions.domain.services import TransactionService
from modules.transactions.presentations.dependencies import get_transaction_service
from modules.transactions.presentations.schemas import SummaryResponse, ExpensesByCategoryResponse

router = APIRouter(
    prefix=settings.api.v1.reports_prefix,
    tags=["Отчёты"],
)


@router.get(
    path="/summary",
    response_model=SummaryResponse,
    summary="Получение общего суммарного дохода и расхода за период",
    description="Возвращает общее суммарное дохода и расхода за период.",
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
    }
)
async def get_summary(
    transaction_service: Annotated[TransactionService, Depends(get_transaction_service)],
    start_date: Optional[datetime] = Query(None, description="Начальная дата периода",
                                           example="2025-03-01T00:00:00"),
    end_date: Optional[datetime] = Query(None, description="Конечная дата периода",
                                         example="2025-04-01T00:00:00"),
) -> SummaryResponse:
    total_income, total_expense = await transaction_service.get_summary(start_date, end_date)
    return SummaryResponse(total_income=total_income, total_expense=total_expense)


@router.get(
    path="/expenses",
    response_model=list[ExpensesByCategoryResponse],
    summary="Получение списка расходов по категориям за период",
    description="Возвращает список всех расходов по категориям за период.",
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
    }
)
async def get_expenses_by_category(
    transaction_service: Annotated[TransactionService, Depends(get_transaction_service)],
    start_date: datetime = Query(..., description="Начальная дата периода", example="2025-03-01T00:00:00"),
    end_date: datetime = Query(..., description="Конечная дата периода", example="2025-04-01T00:00:00"),
) -> list[ExpensesByCategoryResponse]:
    expenses = await transaction_service.get_expenses_by_category(start_date, end_date)
    return [ExpensesByCategoryResponse(category=expense[0], total_expense=expense[1]) for expense in expenses]
