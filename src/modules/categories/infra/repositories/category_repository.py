from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import select, exists, update, delete, func

from modules.categories.domain.interfaces.category_repository_interface import ICategoryRepository
from modules.categories.infra.orms import Category

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class CategoryRepository(ICategoryRepository[Category]):
    model: Category = Category

    def __init__(self, session: "AsyncSession") -> None:
        self.session = session

    async def find_all(
        self,
        limit: int,
        offset: int,
        filter_by: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> tuple[List[Category], int]:
        query = select(self.model)

        if filter_by:
            query = query.where(self.model.title == filter_by)

        if sort_by and sort_order:
            if hasattr(self.model, sort_by):
                field = getattr(self.model, sort_by)
                if sort_order == "asc":
                    query = query.order_by(field.asc())
                elif sort_order == "desc":
                    query = query.order_by(field.desc())
            else:
                raise ValueError(f"Поле {sort_by} не существует в модели")

        total_query = query.with_only_columns(func.count(self.model.id)).order_by(None)
        total = await self.session.execute(total_query)
        total = total.scalar()

        query = query.offset(offset).limit(limit)
        categories = await self.session.execute(query)
        categories = categories.scalars().all()

        return categories, total

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

    async def save(self, title: str) -> Category:
        if await self.exists_by_title(title):
            raise ValueError(f"Category with title {title} already exists.")
        new_category = self.model(title=title)
        self.session.add(new_category)
        await self.session.commit()
        return new_category

    async def update(self, category_id: int, new_title: str) -> Category:
        stmt = (
            update(self.model)
            .where(self.model.id == category_id)
            .values(title=new_title)
        )
        await self.session.execute(stmt)
        await self.session.commit()
        updated_category = await self.find_by_id(category_id)
        return updated_category

    async def delete(self, category_id: int) -> None:
        stmt = delete(self.model).where(self.model.id == category_id)
        await self.session.execute(stmt)
        await self.session.commit()
