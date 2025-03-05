from dataclasses import dataclass
from typing import TypeVar, Generic, Any


VT = TypeVar("VT", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(Generic[VT]):
    value: VT
