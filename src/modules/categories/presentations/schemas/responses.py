from typing import List

from pydantic import BaseModel
from modules.categories.presentations.schemas import CategoryResponse


class BaseSuccessResponse(BaseModel):
    status: str
    message: str


class SuccessCreateCategoryResponse(BaseSuccessResponse):
    data: CategoryResponse


class SuccessUpdateCategoryResponse(BaseSuccessResponse):
    data: CategoryResponse


class PaginatedResponse(BaseModel):
    items: List[CategoryResponse]
    total: int
    page: int
    size: int
    total_pages: int
