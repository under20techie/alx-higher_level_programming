#!/usr/bin/python3
"""Doc
"""
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import (Column, Integer, String)

Base = declarative_base()

class State(Base):
    """ This is the State Class and it inherts from BaseModel """
    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = []
