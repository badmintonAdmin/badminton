import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from config import settings
from api import router as api_router

app = FastAPI()
app.include_router(
    api_router,
    prefix=settings.run.prefix
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True)
