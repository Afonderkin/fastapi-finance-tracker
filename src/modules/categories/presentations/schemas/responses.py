from pydantic import BaseModel
from modules.categories.presentations.schemas import CategoryResponse


class BaseSuccessResponse(BaseModel):
    status: str
    message: str


class SuccessCreateCategoryResponse(BaseSuccessResponse):
    data: CategoryResponse


class SuccessUpdateCategoryResponse(BaseSuccessResponse):
    data: CategoryResponse
