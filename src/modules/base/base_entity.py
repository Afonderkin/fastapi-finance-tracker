from dataclasses import dataclass
from typing import Generic, TypeVar

ID = TypeVar("ID")


@dataclass
class BaseEntity(Generic[ID]):
    id: ID
