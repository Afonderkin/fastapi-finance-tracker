from dataclasses import dataclass

from modules.base import BaseEntity
from modules.categories.domain.value_objects import Title


@dataclass
class CategoryEntity(BaseEntity[int]):
    title: Title

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: 'CategoryEntity') -> bool:
        return self.id == other.id

    def __str__(self) -> str:
        return f"CategoryEntity(id={self.id}, title={self.title})"
