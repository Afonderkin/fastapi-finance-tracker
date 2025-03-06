from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper
from modules.categories.domain.interfaces import ICategoryRepository
from modules.categories.domain.services import CategoryService
from modules.categories.infra.repositories import CategoryRepository


def get_category_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> ICategoryRepository:
    return CategoryRepository(session)


def get_category_service(
    category_repository: Annotated[ICategoryRepository, Depends(get_category_repository)]
) -> CategoryService:
    return CategoryService(category_repository)
