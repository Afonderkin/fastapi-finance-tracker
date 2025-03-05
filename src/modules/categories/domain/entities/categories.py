from dataclasses import dataclass

from modules.base import Base
from modules.categories.domain.value_objects import Title


@dataclass(frozen=True)
class Category(Base[int]):
    title: Title

    def __str__(self) -> str:
        return f"Category(id={self.id}, title={self.title})"
