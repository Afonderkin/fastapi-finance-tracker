from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, TYPE_CHECKING, Optional

from modules.base import BaseModel

if TYPE_CHECKING:
    from modules.categories.infra.orms import Category

ModelType = TypeVar("ModelType", bound=BaseModel)


class ICategoryRepository(ABC, Generic[ModelType]):
    model: ModelType

    @abstractmethod
    async def find_all(
        self,
        limit: int,
        offset: int,
        filter_by: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> "tuple[List[Category], int]":
        raise NotImplementedError()

    @abstractmethod
    async def find_by_id(self, category_id: int) -> "Category | None":
        raise NotImplementedError()

    @abstractmethod
    async def find_by_title(self, title: str) -> "Category | None":
        raise NotImplementedError()

    @abstractmethod
    async def exists_by_title(self, title) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def save(self, title: str) -> "Category":
        raise NotImplementedError()

    @abstractmethod
    async def update(self, category_id: int, new_title: str) -> "Category":
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, category_id: int) -> None:
        raise NotImplementedError()
