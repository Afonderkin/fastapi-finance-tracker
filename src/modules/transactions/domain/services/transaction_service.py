from typing import TYPE_CHECKING

from modules.base import BaseService
from modules.transactions.domain.entities import TransactionEntity

if TYPE_CHECKING:
    from modules.transactions.domain.interfaces import ITransactionRepository


class TransactionService(BaseService[TransactionEntity]):
    def __init__(self, repo: "ITransactionRepository",):
        super(TransactionService, self).__init__(repo)
