from typing import Annotated, Optional

from fastapi import APIRouter, Depends, status, Path, Response, Query

from core.config import settings
from modules.categories.domain.services import CategoryService
from modules.categories.presentations.dependencies import get_category_service
from modules.categories.presentations.schemas import (CategoryResponse, CategoryCreate,
                                                      CategoryUpdate, SuccessUpdateCategoryResponse,
                                                      SuccessCreateCategoryResponse, PaginatedResponse, )

router = APIRouter(
    prefix=settings.api.v1.categories_prefix,
    tags=["Категории"],
)


@router.get(
    path="",
    response_model=PaginatedResponse,
    summary="Получение списка всех категорий",
    description="Возвращает список всех категорий",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def get_categories(
    category_service: Annotated[CategoryService, Depends(get_category_service)],
    page: int = Query(1, description="Номер страницы", ge=1),
    size: int = Query(10, description="Количество элементов на странице", ge=1, le=10),
    sort_by: Optional[str] = Query(None, description="Поле для сортировки"),
    sort_order: Optional[str] = Query(None, description="Порядок сортировки (asc или desc)"),
    filter_by: Optional[str] = Query(None, description="Фильтр по полю"),
) -> PaginatedResponse:
    offset = (page - 1) * size
    categories, total = await category_service.get_all_categories(
        offset=offset,
        limit=size,
        sort_by=sort_by,
        sort_order=sort_order,
        filter_by=filter_by,
    )
    total_pages = (total + size - 1) // size

    return PaginatedResponse(
        items=[CategoryResponse(id=category.id, title=category.title) for category in categories],
        total=total,
        page=page,
        size=size,
        total_pages=total_pages,
    )


@router.get(
    path="/{category_id}",
    response_model=CategoryResponse,
    summary="Получение категории по ID",
    description="Возвращает информацию о категории по указанному ID.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Категория по данному ID не найдена",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def get_category_by_id(
    category_service: Annotated[CategoryService, Depends(get_category_service)],
    category_id: int = Path(..., description="ID категории"),
) -> CategoryResponse:
    category = await category_service.get_category_by_id(category_id)
    return CategoryResponse(id=category.id, title=category.title.value)


@router.post(
    path="",
    response_model=SuccessCreateCategoryResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Создание новой категории",
    description="Создает новую категорию.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def create_category(
    category_service: Annotated[CategoryService, Depends(get_category_service)],
    category: CategoryCreate
) -> SuccessCreateCategoryResponse:
    new_category = await category_service.create_category(title=category.title)
    return SuccessCreateCategoryResponse(
        status="success",
        message="Категория успешно создана",
        data=CategoryResponse(id=new_category.id, title=new_category.title.value),
    )


@router.patch(
    path="/{category_id}",
    response_model=SuccessUpdateCategoryResponse,
    summary="Изменение категории",
    description="Изменяет категорию по указанному ID.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Категория по данному ID не найдена",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def update_category(
    category_service: Annotated[CategoryService, Depends(get_category_service)],
    category: CategoryUpdate,
    category_id: int = Path(..., description="ID категории"),
) -> SuccessUpdateCategoryResponse:
    category = await category_service.update_category_title(category_id, new_title=category.title)
    return SuccessUpdateCategoryResponse(
        status="success",
        message="Категория успешно изменена",
        data=CategoryResponse(id=category.id, title=category.title.value)
    )


@router.delete(
    path="/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удаление категории",
    description="Удаляет категорию по указанному ID.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Категория по данному ID не найдена",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def delete_category(
    category_service: Annotated[CategoryService, Depends(get_category_service)],
    category_id: int = Path(..., description="ID категории"),
):
    await category_service.delete_category(category_id)
    return
