from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


@app.get("/check-db")
def check_db(db: Session = Depends(get_db)):
    return {"status": "success", "message": "Connected to the database successfully!"}
