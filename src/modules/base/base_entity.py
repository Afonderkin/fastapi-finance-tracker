from dataclasses import dataclass
from typing import Generic, TypeVar

ID = TypeVar("ID")


@dataclass(frozen=True)
class Base(Generic[ID]):
    id: ID
