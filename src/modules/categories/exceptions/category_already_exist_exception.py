from dataclasses import dataclass

from modules.base.exceptions import BaseApplicationException


@dataclass(eq=False)
class CategoryAlreadyExistsException(BaseApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f"Категория с заголовком {self.text} уже существует"
