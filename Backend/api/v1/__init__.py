from fastapi import APIRouter
from Backend.core.config import settings
from .users import router as users_router
from .admin import router as admin_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    users_router,
    prefix=settings.api.v1.users,
)

router.include_router(
    admin_router,
    prefix=settings.api.v1.admin,
)
