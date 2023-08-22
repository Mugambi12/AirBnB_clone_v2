#!/usr/bin/python3
"""
This is the City class.
"""

from sqlalchemy import Column, String, Foreigntoken
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """
    Representation of City class.

    Attributes:
        state_id (str): The state ID.
        name (str): The name of the city.
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), Foreigntoken('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
