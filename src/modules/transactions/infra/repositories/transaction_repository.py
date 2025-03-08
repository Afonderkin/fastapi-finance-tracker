from typing import TYPE_CHECKING, Optional, Dict, List

from sqlalchemy import select, func

from modules.base import InMemoryBaseRepository
from modules.base.exceptions import FieldDoesNotExist
from modules.transactions.infra.orms import Transaction

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class InMemoryTransactionRepository(InMemoryBaseRepository[Transaction]):
    model: Transaction = Transaction

    def __init__(self, session: "AsyncSession") -> None:
        super(InMemoryTransactionRepository, self).__init__(session)

    async def find_all(
        self,
        limit: int,
        offset: int,
        filter_by: Optional[Dict[str, any]] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> "tuple[List[Transaction], int]":
        query = select(self.model)

        if filter_by:
            for field, value in filter_by.items():
                if hasattr(self.model, field):
                    query = query.where(getattr(self.model, field) == value)
                elif field == "start_date" and value:
                    query = query.where(self.model.date >= value)
                elif field == "end_date" and value:
                    query = query.where(self.model.date <= value)
                else:
                    raise FieldDoesNotExist(field)

        if sort_by and sort_order:
            if hasattr(self.model, sort_by):
                field = getattr(self.model, sort_by)
                if sort_order == "asc":
                    query = query.order_by(field.asc())
                elif sort_order == "desc":
                    query = query.order_by(field.desc())
            else:
                raise FieldDoesNotExist(sort_by)

        total_query = query.with_only_columns(func.count(self.model.id)).order_by(None)
        total = await self.session.execute(total_query)
        total = total.scalar()

        query = query.offset(offset).limit(limit)
        transactions = await self.session.execute(query)
        transactions = transactions.scalars().all()

        return transactions, total
