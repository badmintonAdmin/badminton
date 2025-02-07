import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings
load_dotenv()


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8080
    prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: str = os.getenv("DATABASE_URL")


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DataBaseConfig = DataBaseConfig()


settings = Settings()
