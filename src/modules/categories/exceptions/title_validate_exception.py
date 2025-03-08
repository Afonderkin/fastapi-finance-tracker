from dataclasses import dataclass

from modules.base import BaseApplicationException


@dataclass(frozen=True, eq=False)
class TitleValidateException(BaseApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f"Ошибка валидации заголовка: {self.text}"
