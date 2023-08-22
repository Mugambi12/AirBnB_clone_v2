#!/usr/bin/python3
"""
This is the Review class.
"""

from sqlalchemy import Column, String, Foreigntoken
from models.base_model import BaseModel, Base

class Review(BaseModel, Base):
    """
    Representation of the Review class.
    """
    if models.selected_storage == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), Foreigntoken('places.id'), nullable=False)
        user_id = Column(String(60), Foreigntoken('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Review"""
        super().__init__(*args, **kwargs)
