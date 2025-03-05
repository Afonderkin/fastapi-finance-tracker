from typing import Generic, TypeVar
from dataclasses import dataclass


ID = TypeVar("ID")


@dataclass(frozen=True)
class Base(Generic[ID]):
    id: ID
