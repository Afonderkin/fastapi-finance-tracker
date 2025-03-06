from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api import router as api_router
from core.config import settings
from core.database import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        lifespan=lifespan,
        debug=settings.app.debug,
        title=settings.app.title,
        description=settings.app.description,
        version=settings.app.version,
    )
    app.include_router(api_router, prefix=settings.api.prefix)

    return app


if __name__ == "__main__":
    uvicorn.run(
        "src.main:create_app",
        factory=True,
        host=settings.app.host,
        port=settings.app.port,
        reload=True,
    )
