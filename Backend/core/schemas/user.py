from pydantic import BaseModel


class UsersBase(BaseModel):
    name: str

class UserCreate(UsersBase):
    pass

class UserGet(UsersBase):
    id: int