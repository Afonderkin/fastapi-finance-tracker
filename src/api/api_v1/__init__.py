from fastapi import APIRouter

from core.config import settings
from modules.categories.presentations.routers import router as category_router
from modules.transactions.presentations.routers import transactions_router
from modules.transactions.presentations.routers import reports_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(category_router)
router.include_router(transactions_router)
router.include_router(reports_router)
