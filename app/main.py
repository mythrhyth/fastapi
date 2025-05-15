# app/main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import app.models as models, app.schemas as schemas, app.crud as crud
from app.database  import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/records/", response_model=schemas.HealthRecord)
def create_health_record(record: schemas.HealthRecordCreate, db: Session = Depends(get_db)):
    return crud.create_health_record(db=db, record=record)

@app.get("/records/{user_id}", response_model=List[schemas.HealthRecord])
def get_health_records(user_id: int, db: Session = Depends(get_db)):
    return crud.get_health_records_by_user(db=db, user_id=user_id)

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return {"users": users}
