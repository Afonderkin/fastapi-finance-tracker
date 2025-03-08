from typing import TYPE_CHECKING

from modules.base import BaseService
from modules.categories.domain.entities import CategoryEntity

if TYPE_CHECKING:
    from modules.categories.domain.interfaces import ICategoryRepository


class CategoryService(BaseService[CategoryEntity]):
    def __init__(
        self,
        repo: "ICategoryRepository",
    ) -> None:
        super(CategoryService, self).__init__(repo)

    async def exists_by_title(self, title):
        return await self.repo.exists_by_title(title)
