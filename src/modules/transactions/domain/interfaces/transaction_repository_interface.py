from abc import ABC
from typing import TypeVar

from modules.base import BaseModel, IBaseRepository

ModelType = TypeVar("ModelType", bound=BaseModel)


class ITransactionRepository(IBaseRepository[ModelType], ABC):
    model: ModelType
