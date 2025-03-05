from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, TYPE_CHECKING

from modules.base import BaseModel

if TYPE_CHECKING:
    from modules.categories.infra.orms import Category

ModelType = TypeVar("ModelType", bound=BaseModel)


class ICategoryRepository(ABC, Generic[ModelType]):
    model: ModelType

    @abstractmethod
    async def find_all(self) -> "List[Category]":
        raise NotImplementedError()

    @abstractmethod
    async def find_by_id(self, category_id: int) -> "Category" | None:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_title(self, title: str) -> "Category" | None:
        raise NotImplementedError()

    @abstractmethod
    async def exists_by_title(self, title) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def save(self, title: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, category_id: int, new_title: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, category_id: int) -> None:
        raise NotImplementedError()
