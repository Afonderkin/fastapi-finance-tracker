from typing import Annotated, Optional

from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper
from modules.categories.domain.interfaces import ICategoryRepository
from modules.categories.domain.services import CategoryService
from modules.categories.infra.repositories import InMemoryCategoryRepository
from modules.categories.presentations.schemas.categories import CategoryFilter


def get_category_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> ICategoryRepository:
    return InMemoryCategoryRepository(session)


def get_category_service(
    category_repository: Annotated[ICategoryRepository, Depends(get_category_repository)]
) -> CategoryService:
    return CategoryService(category_repository)


async def get_filter_by(
    title: Optional[str] = Query(None, description="Фильтр по названию категории")
) -> Optional[CategoryFilter]:
    if title:
        return CategoryFilter(title=title)
    return None
