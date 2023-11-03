#!/usr/bin/python3
"""
Module with class State
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """
    State
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
