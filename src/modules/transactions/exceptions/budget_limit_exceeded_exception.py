from dataclasses import dataclass

from modules.base.exceptions import BaseApplicationException


@dataclass(eq=False)
class BudgetLimitExceededException(BaseApplicationException):
    text: str

    @property
    def message(self) -> str:
        return self.text
