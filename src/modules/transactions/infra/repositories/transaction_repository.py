from typing import TYPE_CHECKING

from modules.base import InMemoryBaseRepository
from modules.transactions.infra.orms import Transaction

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class InMemoryTransactionRepository(InMemoryBaseRepository[Transaction]):
    model: Transaction = Transaction

    def __init__(self, session: "AsyncSession") -> None:
        super(InMemoryTransactionRepository, self).__init__(session)
