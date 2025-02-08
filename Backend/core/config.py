import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings
load_dotenv()


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8080
    prefix: str = "/api"


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DataBaseConfig(BaseModel):
    url: str = os.getenv("DATABASE_URL")
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DataBaseConfig = DataBaseConfig()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
