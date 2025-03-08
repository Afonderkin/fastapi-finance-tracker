from dataclasses import dataclass

from modules.base import BaseApplicationException


@dataclass(frozen=True, eq=False)
class CategoryNotFoundedException(BaseApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f"Категория с id {self.text} не найдена"
