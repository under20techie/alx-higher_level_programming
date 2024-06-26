#!/usr/bin/python3
"""Create user class to map to real table"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """ State Class"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
