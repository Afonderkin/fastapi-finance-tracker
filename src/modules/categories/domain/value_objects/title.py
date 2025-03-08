import re
from dataclasses import dataclass

from modules.base import BaseValueObject


@dataclass
class Title(BaseValueObject[str]):
    value: str

    def __post_init__(self) -> None:
        self._validate_title(self.value)

    @staticmethod
    def _validate_title(title) -> None:
        if not title:
            raise ValueError("Title cannot be empty")
        if not re.match(r'^[A-Za-zА-Яа-я\s]+$', title):
            raise ValueError("Title must only contain alphabetic characters (Latin, Cyrillic) and spaces")
        if len(title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
