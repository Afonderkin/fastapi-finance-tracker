from typing import TYPE_CHECKING

from modules.base import BaseService

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from modules.categories.domain.interfaces import ICategoryRepository


class CategoryService(BaseService["ICategoryRepository", "CategoryEntity"]):
    def __init__(
        self,
        session: "AsyncSession",
        repo: "ICategoryRepository",
    ) -> None:
        super(CategoryService, self).__init__(session, repo)

    async def get_by_title(self, title: str) -> "CategoryEntity | None":
        category = await self.repo.find_by_title(title)
        if category:
            return category.to_entity()
        return None
