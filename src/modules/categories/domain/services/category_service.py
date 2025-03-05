from typing import TYPE_CHECKING

from modules.categories.domain.entities import CategoryEntity
from modules.categories.infra.orms import Category

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from modules.categories.domain.interfaces import ICategoryRepository


class CategoryService:
    def __init__(
        self,
        session: AsyncSession,
        repo: ICategoryRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def get_all_categories(self) -> list[CategoryEntity]:
        categories = [category.to_entity() for category in (await self.repo.find_all())]
        return categories

    async def get_category_by_id(self, category_id: int) -> CategoryEntity | None:
        category = await self.repo.find_by_id(category_id)
        if category:
            return category.to_entity()
        return None

    async def get_category_by_title(self, title: str) -> CategoryEntity | None:
        category = await self.repo.find_by_title(title)
        if category:
            return category.to_entity()
        return None

    async def create_category(self, title: str) -> None:
        await self.repo.save(title=title)

    async def update_category_title(self, category_id: int, new_title: str) -> None:
        await self.repo.update(category_id=category_id, new_title=new_title)

    async def delete_category(self, category_id: int) -> None:
        await self.repo.delete(category_id=category_id)
