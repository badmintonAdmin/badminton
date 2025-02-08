from pydantic import BaseModel


class UsersBase(BaseModel):
    name: str
