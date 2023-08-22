#!/usr/bin/python3
"""
Contains the DBStorage class for interacting with a MySQL database.
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Dictionary to map class names to actual classes
classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        User = getenv('HBNB_MYSQL_USER')
        Passcode = getenv('HBNB_MYSQL_PWD')
        Host = getenv('HBNB_MYSQL_HOST')
        Db = getenv('HBNB_MYSQL_DB')
        Env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(User,
                                             Passcode,
                                             Host,
                                             Db))
        if Env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        new_dictionary = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    token = obj.__class__.__name__ + '.' + obj.id
                    new_dictionary[token] = obj
        return new_dictionary

    # ... (rest of the methods)

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()
