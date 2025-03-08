from dataclasses import dataclass

from modules.base import BaseValueObject
from modules.base.exceptions import ValidateException


@dataclass
class Description(BaseValueObject[str]):
    value: str

    def __post_init__(self):
        self._validate(self.value)

    @staticmethod
    def _validate(value):
        if len(value) > 255:
            raise ValidateException("Описание не должно превышать 255 символов")
