__all__ = (
    "transactions_router",
    "reports_router",
    "budgets_router",
)

from modules.transactions.presentations.routers.report_routers import (
    router as reports_router,
)
from modules.transactions.presentations.routers.transaction_routers import (
    router as transactions_router,
)
from modules.transactions.presentations.routers.budget_routers import (
    router as budgets_router,
)
