
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models_energy import BuildingData
from pydantic import BaseModel
from typing import List
from datetime import date

router = APIRouter()

class BuildingDataCreate(BaseModel):
    building_id: int
    timestamp: date
    electricity_kwh: float
    water_tons: float
    gas_m3: float
    co2_tons: float

class BuildingDataOut(BuildingDataCreate):
    id: int
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add", response_model=BuildingDataOut)
def add_data(entry: BuildingDataCreate, db: Session = Depends(get_db)):
    data = BuildingData(**entry.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@router.get("/history/{building_id}", response_model=List[BuildingDataOut])
def get_history(building_id: int, db: Session = Depends(get_db)):
    return db.query(BuildingData).filter(BuildingData.building_id == building_id).order_by(BuildingData.timestamp).all()
