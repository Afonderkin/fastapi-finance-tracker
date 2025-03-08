from dataclasses import dataclass

from modules.base.exceptions import BaseApplicationException


@dataclass(frozen=True, eq=False)
class FieldDoesNotExist(BaseApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f"Поле {self.text} не существует в модели"
