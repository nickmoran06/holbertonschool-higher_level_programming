#!/usr/bin/python3
"""
Module that contains the City Class
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Representation of a City
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
