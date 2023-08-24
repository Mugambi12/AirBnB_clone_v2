#!/usr/bin/python3
""" Module: state - holds class State """

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import shlex


class State(BaseModel, Base):
    """
    Representation of the State class.
    """

    if models.selected_storage == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the State class.
        """
        super().__init__(*args, **kwargs)

    if models.selected_storage != "db":
        @property
        def cities(self):
            """
            Getter for a list of city instances related to the state.
            """
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        else:
            def cities(self):
                """
                Getter for a list of city instances related to the state.
                """
                var = models.storage.all()
                lista = []
                result = []
                for key in var:
                    city = key.replace('.', ' ')
                    city = shlex.split(city)
                    if (city[0] == 'City'):
                        lista.append(var[key])
                for elem in lista:
                    if (elem.state_id == self.id):
                        result.append(elem)
                return (result)
