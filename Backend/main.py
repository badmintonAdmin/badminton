import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from core.config import settings
from core.models import db_helper
from api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan
)
main_app.include_router(
    api_router,
    prefix=settings.run.prefix
)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True)
