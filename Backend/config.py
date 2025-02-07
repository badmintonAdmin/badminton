import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings
load_dotenv()


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8080


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db_url: str = os.getenv("DATABASE_URL")


settings = Settings()
