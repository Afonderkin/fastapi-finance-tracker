from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from modules.transactions.domain.entities import TransactionType


class TransactionBase(BaseModel):
    amount: float
    description: Optional[str] = None
    transaction_type: TransactionType
    date: datetime
    category_id: int


class TransactionResponse(BaseModel):
    id: int
    amount: float
    description: Optional[str] = None
    transaction_type: str
    date: datetime
    category_id: int


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    transaction_type: Optional[TransactionType] = None
    date: Optional[datetime] = None
    category_id: Optional[int] = None
