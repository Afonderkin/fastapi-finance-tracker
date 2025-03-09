from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypeVar, Optional

from modules.base import BaseModel, IBaseRepository

ModelType = TypeVar("ModelType", bound=BaseModel)


class IBudgetRepository(IBaseRepository[ModelType], ABC):
    model: ModelType

    @abstractmethod
    async def get_budget_for_category(
        self,
        category_id: int,
        period_start: datetime,
        period_end: datetime,
    ) -> Optional[ModelType]:
        raise NotImplementedError()

    @abstractmethod
    async def get_actual_expenses(
        self,
        category_id: int,
        period_start: datetime,
        period_end: datetime,
    ) -> float:
        raise NotImplementedError()
