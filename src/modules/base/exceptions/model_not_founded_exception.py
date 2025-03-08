from dataclasses import dataclass

from modules.base.exceptions import BaseApplicationException


@dataclass(eq=False)
class ModelNotFoundException(BaseApplicationException):
    model: str
    id: str

    @property
    def message(self) -> str:
        return f"{self.model} с id {self.id} не найдена"
