from dataclasses import dataclass

from modules.base import BaseApplicationException


@dataclass(frozen=True, eq=False)
class CategoryAlreadyExistsException(BaseApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f"Категория с заголовком {self.text} уже существует"
