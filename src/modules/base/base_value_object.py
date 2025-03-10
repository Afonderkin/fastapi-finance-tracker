from dataclasses import dataclass
from typing import TypeVar, Generic, Any


VT = TypeVar("VT", bound=Any)


@dataclass
class BaseValueObject(Generic[VT]):
    value: VT

    def __str__(self) -> VT:
        return self.value
