from dataclasses import dataclass

from modules.base import BaseEntity
from modules.categories.domain.value_objects import Title


@dataclass(frozen=True)
class CategoryEntity(BaseEntity[int]):
    title: Title

    def __str__(self) -> str:
        return f"CategoryEntity(id={self.id}, title={self.title})"
