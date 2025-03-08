from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class BaseApplicationException(Exception):
    @property
    def message(self) -> str:
        return "Произошла ошибка приложения"

    def __str__(self):
        return self.message

if 1 == 1:
    raise BaseApplicationException()
