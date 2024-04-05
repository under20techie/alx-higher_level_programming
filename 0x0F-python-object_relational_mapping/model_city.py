"""Create user class to map to real table"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """ State Class"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
