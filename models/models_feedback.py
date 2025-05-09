
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import date

class FeedbackLog(Base):
    __tablename__ = "feedback_log"
    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    strategy_text = Column(String)
    accepted = Column(Boolean)
    timestamp = Column(Date, default=date.today)

    building = relationship("Building")
    user = relationship("User")
