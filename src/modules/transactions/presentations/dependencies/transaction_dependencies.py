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
) -> Optional[TransactionFilter]:
    if transaction_type:
        return TransactionFilter(transaction_type=transaction_type)
    return None
