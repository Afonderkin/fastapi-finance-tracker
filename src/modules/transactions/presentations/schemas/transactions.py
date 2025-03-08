from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

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


class TransactionFilter(BaseModel):
    transaction_type: Optional[TransactionType] = Field(
        default=None,
        description="Фильтрация транзакции по типу транзакции",
        examples=["Доход", "Расход"]
    )
    category_id: Optional[int] = Field(
        default=None,
        description="Фильтрация транзакции по идентификатору категории",
        examples=[1, 2]
    )
    start_date: Optional[datetime] = Field(
        default=None,
        description="Фильтрация по начальной дате",
        examples=["2023-01-01T00:00:00"]
    )
    end_date: Optional[datetime] = Field(
        default=None,
        description="Фильтрация по конечной дате",
        examples=["2023-12-31T23:59:59"]
    )
