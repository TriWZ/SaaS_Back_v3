
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Building
from pydantic import BaseModel
from typing import List

router = APIRouter()

class BuildingCreate(BaseModel):
    user_id: int
    name: str
    address: str
    area_sqft: int

class BuildingOut(BaseModel):
    id: int
    user_id: int
    name: str
    address: str
    area_sqft: int
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add", response_model=BuildingOut)
def add_building(b: BuildingCreate, db: Session = Depends(get_db)):
    new_building = Building(**b.dict())
    db.add(new_building)
    db.commit()
    db.refresh(new_building)
    return new_building

@router.get("/list/{user_id}", response_model=List[BuildingOut])
def list_buildings(user_id: int, db: Session = Depends(get_db)):
    return db.query(Building).filter(Building.user_id == user_id).all()
