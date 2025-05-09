
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models_feedback import FeedbackLog
from pydantic import BaseModel
from typing import List
from datetime import date

router = APIRouter()

class FeedbackEntry(BaseModel):
    building_id: int
    user_id: int
    strategy_text: str
    accepted: bool

class FeedbackOut(FeedbackEntry):
    id: int
    timestamp: date
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add", response_model=FeedbackOut)
def add_feedback(fb: FeedbackEntry, db: Session = Depends(get_db)):
    log = FeedbackLog(**fb.dict())
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

@router.get("/{building_id}", response_model=List[FeedbackOut])
def get_feedback(building_id: int, db: Session = Depends(get_db)):
    return db.query(FeedbackLog).filter(FeedbackLog.building_id == building_id).all()
