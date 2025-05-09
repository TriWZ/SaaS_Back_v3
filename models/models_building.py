
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models import User

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    address = Column(String)
    area_sqft = Column(Integer)

    user = relationship("User")
