from fastapi import APIRouter, Depends
from typing import Annotated
from Backend.crud.users import get_all_users,create_user
from Backend.core.schemas.user import UserGet, UserCreate
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

@router.post("/add",response_model=UserGet)
async def add_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user: UserCreate
):
    added_user = await create_user(session=session,user_create=user)
    return added_user