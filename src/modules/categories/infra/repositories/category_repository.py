from typing import TYPE_CHECKING

from sqlalchemy import select, exists

from modules.base import InMemoryBaseRepository
from modules.categories.infra.orms import Category

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class InMemoryCategoryRepository(InMemoryBaseRepository[Category]):
    model: Category = Category

    def __init__(self, session: "AsyncSession") -> None:
        super(InMemoryCategoryRepository, self).__init__(session)

    async def exists_by_title(self, title) -> bool:
        stmt = select(exists().where(self.model.title == title))
        result = await self.session.execute(stmt)
        return result.scalar()
