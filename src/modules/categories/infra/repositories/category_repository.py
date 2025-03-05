from typing import TYPE_CHECKING, List

from sqlalchemy import select, exists, update, delete

from modules.categories.domain.interfaces.category_repository_interface import ICategoryRepository
from modules.categories.infra.orms import Category

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class CategoryRepository(ICategoryRepository[Category]):
    model: Category = Category

    def __init__(self, session: "AsyncSession") -> None:
        self.session = session

    async def find_all(self) -> List[Category]:
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def find_by_id(self, category_id: int) -> Category | None:
        stmt = select(self.model).where(self.model.id == category_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def find_by_title(self, title: str) -> Category | None:
        stmt = select(self.model).where(self.model.title == title)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def exists_by_title(self, title) -> bool:
        stmt = select(exists().where(self.model.title == title))
        result = await self.session.execute(stmt)
        return result.scalar()

    async def save(self, title: str) -> None:
        if await self.exists_by_title(title):
            raise ValueError(f"Category with title {title} already exists.")
        new_category = self.model(title=title)
        self.session.add(new_category)
        await self.session.commit()

    async def update(self, category_id: int, new_title: str) -> None:
        stmt = (
            update(self.model)
            .where(self.model.id == category_id)
            .values(title=new_title)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def delete(self, category_id: int) -> None:
        stmt = delete(self.model).where(self.model.id == category_id)
        await self.session.execute(stmt)
        await self.session.commit()
