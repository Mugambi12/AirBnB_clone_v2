#!/usr/bin/python3
"""Module: user - holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """
    Representation of the User class.
    """
    if models.selected_storage == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
        reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")

    else:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = []
        reviews = []

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the User class.
        """
        super().__init__(*args, **kwargs)

        if self.password and models.selected_storage == 'db':
            hashed_password = hashlib.md5(self.password.encode("utf-8"))
            self.password = hashed_password.hexdigest()
