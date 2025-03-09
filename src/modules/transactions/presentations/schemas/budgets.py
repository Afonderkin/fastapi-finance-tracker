from datetime import datetime
from pydantic import BaseModel


class BudgetCreate(BaseModel):
    category_id: int
    limit: float
    period_start: datetime
    period_end: datetime


class BudgetResponse(BaseModel):
    id: int
    category_id: int
    limit: float
    period_start: datetime
    period_end: datetime
    actual_expenses: float
    remaining_budget: float
