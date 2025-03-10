from typing import List

from pydantic import BaseModel
from modules.transactions.presentations.schemas.transactions import TransactionResponse


class BaseSuccessResponse(BaseModel):
    status: str
    message: str


class SuccessCreateTransactionResponse(BaseSuccessResponse):
    data: TransactionResponse


class SuccessUpdateTransactionResponse(BaseSuccessResponse):
    data: TransactionResponse


class PaginatedResponse(BaseModel):
    items: List[TransactionResponse]
    total: int
    page: int
    size: int
    total_pages: int


class SummaryResponse(BaseModel):
    total_income: float
    total_expense: float


class ExpensesByCategoryResponse(BaseModel):
    category: str
    total_expense: float
