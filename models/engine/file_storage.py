#!/usr/bin/python3
"""
Contains the FileStorage class for serializing and deserializing instances to/from a JSON file.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Dictionary to map class names to actual classes
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dictionary = {}
            for token, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dictionary[token] = value
            return new_dictionary
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with token <obj class name>.id"""
        if obj is not None:
            token = obj.__class__.__name__ + "." + obj.id
            self.__objects[token] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for token in self.__objects:
            json_objects[token] = self.__objects[token].to_dict(save_check=True)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                j_file = json.load(f)
            for token in j_file:
                self.__objects[token] = classes[j_file[token]["__class__"]](**j_file[token])
        except:
            pass

    def get(self, cls, id):
        """Retrieving object by class and/or id
        """
        token = cls.__name__ + '.' + id

        if token in self.__objects:
            return self.__objects[token]
        else:
            return None

    def count(self, cls=None):
        """Return count of objects in storage
        """
        return len(self.all(cls))

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            token = obj.__class__.__name__ + '.' + obj.id
            if token in self.__objects:
                del self.__objects[token]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
