from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class HealthRecordBase(BaseModel):
    weight: float
    height: float
    blood_pressure: str

class HealthRecordCreate(HealthRecordBase):
    user_id: int

class HealthRecord(HealthRecordBase):
    id: int
    user_id: int
    date: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    records: List[HealthRecord] = []

    class Config:
        orm_mode = True

