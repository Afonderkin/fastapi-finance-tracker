from typing import TYPE_CHECKING, Optional, List

from modules.categories.exceptions import CategoryAlreadyExistsException

if TYPE_CHECKING:
    from modules.categories.domain.interfaces import ICategoryRepository
    from modules.categories.domain.entities import CategoryEntity


class CategoryService:
    def __init__(
        self,
        repo: "ICategoryRepository",
    ) -> None:
        self.repo = repo

    async def get_all_categories(
        self,
        limit: int,
        offset: int,
        filter_by: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> "tuple[List[CategoryEntity], int]":

        categories, total = await self.repo.find_all(
            limit=limit,
            offset=offset,
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return [category.to_entity() for category in categories], total

    async def get_category_by_id(self, category_id: int) -> "CategoryEntity | None":
        category = await self.repo.find_by_id(category_id)
        if category:
            return category.to_entity()
        return None

    async def create_category(self, title: str) -> "CategoryEntity":
        if await self.repo.exists_by_title(title):
            raise CategoryAlreadyExistsException(title)
        category = await self.repo.save(title=title)
        return category.to_entity()

    async def update_category_title(self, category_id: int, new_title: str) -> "CategoryEntity":
        category = await self.repo.update(category_id, title=new_title)
        return category.to_entity()

    async def delete_category(self, category_id: int) -> None:
        await self.repo.delete(category_id)
