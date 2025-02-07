from pydantic import BaseModel, Field, EmailStr


class Users_add_shema(BaseModel):
    category_id: int
    name: str
    email: str
    invate: str
    rang: float
    level: int


class Users_shema(Users_add_shema):
    id: int
