from fastapi import APIRouter, Depends
from typing import Annotated
from Backend.crud.users import get_all_users
from Backend.core.schemas.user import UserGet
from sqlalchemy.ext.asyncio import AsyncSession

from Backend.core.models import db_helper

router = APIRouter(tags=["users"])

@router.get("",response_model=list[UserGet])
async def get_users(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
):
    users = await get_all_users(session=session)
    return users