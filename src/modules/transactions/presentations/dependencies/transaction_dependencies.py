from datetime import datetime
from typing import Annotated, Optional

from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper
from modules.transactions.domain.entities import TransactionType
from modules.transactions.domain.interfaces import ITransactionRepository
from modules.transactions.domain.services import TransactionService
from modules.transactions.infra.repositories import InMemoryTransactionRepository
from modules.transactions.presentations.schemas.transactions import TransactionFilter


def get_transaction_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> ITransactionRepository:
    return InMemoryTransactionRepository(session)


def get_transaction_service(
    category_repository: Annotated[ITransactionRepository, Depends(get_transaction_repository)]
) -> TransactionService:
    return TransactionService(category_repository)


async def get_filter_by(
    transaction_type: Optional[TransactionType] = Query(None, description="Фильтр по типу транзакции"),
    category_id: Optional[int] = Query(None, description="Фильтр по категории транзакции"),
    start_date: Optional[datetime] = Query(None, description="Фильтр по начальной дате",
                                           example="2023-01-01T00:00:00"),
    end_date: Optional[datetime] = Query(None, description="Фильтр по конечной дате",
                                         example="2023-01-01T00:00:00"),
) -> Optional[TransactionFilter]:
    filter_params = {}
    if transaction_type:
        filter_params["transaction_type"] = transaction_type
    if category_id:
        filter_params["category_id"] = category_id
    if start_date:
        filter_params["start_date"] = start_date
    if end_date:
        filter_params["end_date"] = end_date

    if filter_params:
        return TransactionFilter(**filter_params)
    return None
