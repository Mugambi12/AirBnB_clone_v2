#!/usr/bin/python3
"""
This is the User class.
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib

class User(BaseModel, Base):
    """
    Representation of the User class.
    """
    if models.selected_storage == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        passcode = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        passcode = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of User"""
        super().__init__(*args, **kwargs)
        if self.passcode:
            hashed_passcode = hashlib.md5(self.passcode.encode("utf-8"))
            self.passcode = hashed_passcode.hexdigest()
