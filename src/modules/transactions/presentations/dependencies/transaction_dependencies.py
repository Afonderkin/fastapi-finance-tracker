from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper
from modules.transactions.domain.interfaces import ITransactionRepository
from modules.transactions.domain.services import TransactionService
from modules.transactions.infra.repositories import InMemoryTransactionRepository


def get_transaction_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> ITransactionRepository:
    return InMemoryTransactionRepository(session)


def get_transaction_service(
    category_repository: Annotated[ITransactionRepository, Depends(get_transaction_repository)]
) -> TransactionService:
    return TransactionService(category_repository)
