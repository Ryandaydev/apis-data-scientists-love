"""FastAPI program - Chapter 4"""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, schemas
from database import SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {
        "message": "API health check successful",
        "success": True,
        "status_code": None
        }

@app.get("/")
async def root():
    return {"message": "API health check successful"}


@app.get("/v0/players/", response_model=list[schemas.Player])
def read_players(db: Session = Depends(get_db)):
    players = crud.get_players(db)
    return players


