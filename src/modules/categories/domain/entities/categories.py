from dataclasses import dataclass

from modules.base import Base
from modules.categories.domain.value_objects import Title


@dataclass(frozen=True)
class Category(Base[int]):
    title: Title
