#!/usr/bin/python3
"""Create user class to map to real table
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
