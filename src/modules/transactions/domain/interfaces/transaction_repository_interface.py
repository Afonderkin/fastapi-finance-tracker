from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypeVar, Optional, List

from modules.base import BaseModel, IBaseRepository

ModelType = TypeVar("ModelType", bound=BaseModel)


class ITransactionRepository(IBaseRepository[ModelType], ABC):
    model: ModelType

    @abstractmethod
    async def get_summary(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> tuple[float, float]:
        raise NotImplementedError()

    @abstractmethod
    async def get_expenses_by_category(
        self,
        start_date: datetime,
        end_date: datetime,
    ) -> List[tuple[str, float]]:
        raise NotImplementedError()
