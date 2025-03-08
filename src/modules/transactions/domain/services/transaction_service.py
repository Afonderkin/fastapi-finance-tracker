from datetime import datetime
from typing import TYPE_CHECKING, Optional, List, Dict

if TYPE_CHECKING:
    from modules.transactions.domain.entities import TransactionEntity
    from modules.transactions.domain.interfaces import ITransactionRepository


class TransactionService:
    def __init__(self, repo: "ITransactionRepository",):
        self.repo = repo

    async def get_all_transactions(
        self,
        limit: int,
        offset: int,
        filter_by: Optional[Dict[str, any]] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> "tuple[List[TransactionEntity], int]":
        transactions, total = await self.repo.find_all(
            limit=limit,
            offset=offset,
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return [transaction.to_entity() for transaction in transactions], total

    async def get_transaction_by_id(self, transaction_id: int) -> "TransactionEntity | None":
        transaction = await self.repo.find_by_id(transaction_id)
        if transaction:
            return transaction.to_entity()
        return None

    async def create_transaction(
        self,
        amount: float,
        description: str,
        transaction_type: str,
        date: datetime,
        category_id: int,
    ) -> "TransactionEntity":
        transaction = await self.repo.save(
            amount=amount,
            description=description,
            transaction_type=transaction_type,
            date=date,
            category_id=category_id,
        )
        return transaction.to_entity()

    async def update_transaction(
        self,
        transaction_id: int,
        **update_data,
    ) -> "TransactionEntity":
        transaction = await self.repo.update(
            transaction_id,
            **update_data,
        )
        return transaction.to_entity()

    async def delete_transaction(self, transaction_id: int) -> None:
        await self.repo.delete(transaction_id)
