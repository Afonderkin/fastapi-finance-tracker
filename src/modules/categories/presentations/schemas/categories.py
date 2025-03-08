from typing import Optional

from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    title: str


class CategoryResponse(BaseModel):
    id: int
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryFilter(BaseModel):
    title: Optional[str] = Field(
        default=None,
        description="Фильтр по названию категории",
        examples=["Продукты"],
    )
