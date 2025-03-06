from fastapi import APIRouter

from core.config import settings
from modules.categories.presentations.routers import router as category_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(category_router)
