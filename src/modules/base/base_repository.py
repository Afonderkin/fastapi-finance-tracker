from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional, TYPE_CHECKING, Dict

from sqlalchemy import select, func, update, delete

from modules.base import BaseModel
from modules.base.exceptions import FieldDoesNotExist, ModelNotFoundException

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType", bound=BaseModel)


class IBaseRepository(ABC, Generic[ModelType]):
    model: ModelType

    @abstractmethod
    async def find_all(
        self,
        limit: int,
        offset: int,
        filter_by: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> "tuple[List[ModelType], int]":
        raise NotImplementedError()

    @abstractmethod
    async def find_by_id(self, model_id: int) -> "ModelType | None":
        raise NotImplementedError()

    @abstractmethod
    async def save(self, **data) -> "ModelType":
        raise NotImplementedError()

    @abstractmethod
    async def update(self, model_id: int, **new_data: str) -> "ModelType":
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, model_id: int) -> None:
        raise NotImplementedError()


class InMemoryBaseRepository(IBaseRepository[ModelType]):
    model: ModelType = BaseModel

    def __init__(self, session: "AsyncSession") -> None:
        self.session = session

    async def find_all(
        self,
        limit: int,
        offset: int,
        filter_by: Optional[Dict[str, any]] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> "tuple[List[ModelType], int]":
        query = select(self.model)

        if filter_by:
            for field, value in filter_by.items():
                if hasattr(self.model, field):
                    query = query.where(getattr(self.model, field) == value)
                else:
                    raise FieldDoesNotExist(field)

        if sort_by and sort_order:
            if hasattr(self.model, sort_by):
                field = getattr(self.model, sort_by)
                if sort_order == "asc":
                    query = query.order_by(field.asc())
                elif sort_order == "desc":
                    query = query.order_by(field.desc())
            else:
                raise FieldDoesNotExist(sort_by)

        total_query = query.with_only_columns(func.count(self.model.id)).order_by(None)
        total = await self.session.execute(total_query)
        total = total.scalar()

        query = query.offset(offset).limit(limit)
        model_list = await self.session.execute(query)
        model_list = model_list.scalars().all()

        return model_list, total

    async def find_by_id(self, model_id: int) -> "ModelType | None":
        stmt = select(self.model).where(self.model.id == model_id)
        result = await self.session.execute(stmt)
        result = result.scalar_one_or_none()
        if result:
            return result
        return None

    async def save(self, **data) -> "ModelType":
        model = self.model(**data)
        self.session.add(model)
        await self.session.commit()
        return model

    async def update(self, model_id: int, **new_data: str) -> "ModelType":
        stmt = (
            update(self.model)
            .where(self.model.id == model_id)
            .values(**new_data)
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, model_id: int) -> None:
        category = await self.find_by_id(model_id)
        if not category:
            raise ModelNotFoundException(self.model, model_id)
        stmt = delete(self.model).where(self.model.id == model_id)
        await self.session.execute(stmt)
        await self.session.commit()
