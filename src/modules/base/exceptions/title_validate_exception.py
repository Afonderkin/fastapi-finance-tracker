from dataclasses import dataclass

from modules.base.exceptions import BaseApplicationException


@dataclass(eq=False)
class ValidateException(BaseApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f"Ошибка валидации: {self.text}"
