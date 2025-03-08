import re
from dataclasses import dataclass

from modules.base import BaseValueObject
from modules.base.exceptions import ValidateException


@dataclass
class Title(BaseValueObject[str]):
    value: str

    def __post_init__(self) -> None:
        self._validate_title(self.value)

    @staticmethod
    def _validate_title(title) -> None:
        if not title:
            raise ValidateException("Заголовок не может быть пустым")
        if not re.match(r'^[A-Za-zА-Яа-я\s]+$', title):
            raise ValidateException("Заголовок должен содержать только буквы (латиницу, кириллицу) и пробелы")
        if len(title) > 100:
            raise ValidateException("Заголовок не должен превышать 100 символов")
