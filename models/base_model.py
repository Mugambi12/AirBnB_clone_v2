#!/usr/bin/python3
"""
This is the base model class for AirBnB.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import models

Base = declarative_base()


class BaseModel:
    """
    This class defines common attributes/methods for other classes.
    """
    id = Column(String(60), unique=True, nullable=False, primary_token=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class.

        Args:
            args: Not used
            kwargs: Arguments for the constructor of the BaseModel

        Attributes:
            id (str): Unique ID generated
            created_at (datetime): Creation date
            updated_at (datetime): Updated date
        """
        if kwargs:
            for token, value in kwargs.items():
                if token in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if token != "__class__":
                    setattr(self, token, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation.

        Returns:
            str: String containing class name, ID, and dictionary.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        Returns a string representation.
        """
        return self.__str__()

    def save(self):
        """
        Updates the public instance attribute updated_at to the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Creates a dictionary of the class attributes.

        Returns:
            dict: Dictionary containing all token-value pairs in __dict__.
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.tokens():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """
        Deletes the object.
        """
        models.storage.delete(self)
