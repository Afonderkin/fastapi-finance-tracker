from abc import ABC, abstractmethod
from typing import TypeVar

from modules.base import BaseModel, IBaseRepository

ModelType = TypeVar("ModelType", bound=BaseModel)


class ICategoryRepository(IBaseRepository[ModelType], ABC):
    model: ModelType

    @abstractmethod
    async def exists_by_title(self, title) -> bool:
        raise NotImplementedError()
