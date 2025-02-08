from fastapi import APIRouter, Depends
from typing import Annotated
from Backend.crud.users import get_all_users, create_user
from Backend.core.schemas.user import UserGet, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

from Backend.core.models import db_helper

router = APIRouter(tags=["admin"])


@router.get("")
async def admins():
    return {"ok"}
