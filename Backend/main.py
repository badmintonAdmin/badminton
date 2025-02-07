from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.future import select
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy.orm import Session
from database import get_db, get_engine
from createTables import setup_users
from users import Users_add_shema
from models import UsersModel

app = FastAPI()


@app.get(
    "/check-db",
    tags=["BD check"]
)
def check_db(db: Session = Depends(get_db)):
    return {"status": "success", "message": "Connected to the database successfully!"}


@app.get(
    "/test/{id}",
    tags=["test"]
)
def test(id: int):
    if id < 2:
        return {'ok'}
    else:
        raise HTTPException(status_code=404, detail='noway')


class newTest(BaseModel):
    title: str
    mix: int = Field(gt=5)


@app.post(
    '/tests_post'
)
def create_tests(new_test: newTest):
    return {'yes'}


SessionDep = Annotated[AsyncSession, Depends(get_db)]


@app.post(
    '/add_users'
)
async def add_users(user_data: Users_add_shema, session: SessionDep):
    new_users = UsersModel(
        category_id=user_data.category_id,
        name=user_data.name,
        email=user_data.email,
        invate=user_data.invate,
        rang=user_data.rang,
        level=user_data.level
    )
    session.add(new_users)
    await session.commit()
    return {'yes'}


@app.get(
    '/get_users'
)
async def get_users(session: SessionDep):
    query = select(UsersModel)
    result = await session.execute(query)
    return result.scalars().all()


@app.post(
    '/create_users'
)
async def create_users():
    await setup_users()
    return {'yes'}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
