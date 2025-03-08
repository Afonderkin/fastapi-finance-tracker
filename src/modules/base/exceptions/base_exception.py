from dataclasses import dataclass


@dataclass(eq=False)
class BaseApplicationException(Exception):
    @property
    def message(self) -> str:
        return "Произошла ошибка приложения"

    def __str__(self):
        return self.message
