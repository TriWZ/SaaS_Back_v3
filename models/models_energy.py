
from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class BuildingData(Base):
    __tablename__ = "building_data"
    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    timestamp = Column(Date)
    electricity_kwh = Column(Float)
    water_tons = Column(Float)
    gas_m3 = Column(Float)
    co2_tons = Column(Float)

    building = relationship("Building")
