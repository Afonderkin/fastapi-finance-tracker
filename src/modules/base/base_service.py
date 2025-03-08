from typing import TYPE_CHECKING, Optional, List, Dict, Generic, TypeVar

from modules.base import BaseEntity

if TYPE_CHECKING:
    from modules.base.base_repository import IBaseRepository

EntityType = TypeVar("EntityType", bound=BaseEntity)


class BaseService(Generic[EntityType]):
    def __init__(
        self,
        repo: "IBaseRepository",
    ) -> None:
        self.repo = repo

    async def get_all(
        self,
        limit: int,
        offset: int,
        filter_by: Optional[Dict[str, any]] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> tuple[List["EntityType"], int]:

        entities, total = await self.repo.find_all(
            limit=limit,
            offset=offset,
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return [entity.to_entity() for entity in entities], total

    async def get_by_id(self, entity_id: int) -> "EntityType | None":
        entity = await self.repo.find_by_id(entity_id)
        if entity:
            return entity.to_entity()
        return None

    async def create(self, **data) -> "EntityType":
        entity = await self.repo.save(**data)
        return entity.to_entity()

    async def update(
        self,
        entity_id: int,
        **update_data,
    ) -> "EntityType":
        entity = await self.repo.update(
            entity_id,
            **update_data,
        )
        return entity.to_entity()

    async def delete(self, entity_id: int) -> None:
        await self.repo.delete(entity_id)
