from pydantic import BaseModel


class CategoryBase(BaseModel):
    title: str


class CategoryResponse(BaseModel):
    id: int
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass
