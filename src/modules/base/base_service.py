from typing import Generic, TypeVar, TYPE_CHECKING

from modules.base import BaseEntity

RepoType = TypeVar("RepoType")
Entity = TypeVar("Entity", bound=BaseEntity)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class BaseService(Generic[RepoType, Entity]):
    def __init__(
            self,
            session: "AsyncSession",
            repo: RepoType,
    ) -> None:
        self.session = session
        self.repo = repo

    async def get_all(self) -> list[Entity]:
        entities = [entity.to_entity() for entity in (await self.repo.find_all())]
        return entities

    async def get_by_id(self, entity_id: int) -> Entity | None:
        entity = await self.repo.find_by_id(entity_id)
        if entity:
            return entity.to_entity()
        return None

    async def create(self, **kwargs) -> None:
        await self.repo.save(**kwargs)

    async def update(self, entity_id: int, **kwargs) -> None:
        await self.repo.update(entity_id, **kwargs)

    async def delete(self, entity_id) -> None:
        await self.repo.delete(entity_id)
