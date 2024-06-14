#!/usr/bin/python3
"""Creating class amenities"""
import uuid
from datetime import datetime
from persistence.DataManager import DataManager


class Amenity(DataManager):
    """"Amenity class"""
    def __init__(self, name):
        """Init method"""
        self.__name = name
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated_at = self.created_at

    @property
    def id(self):
        """Return id"""
        return self.__id

    @property
    def created_at(self):
        """Return created_at"""
        return self.__created_at

    @property
    def updated_at(self):
        """Return updated_at"""
        return self.__updated_at

    @property
    def name(self):
        """Return name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Set name"""
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value:
            raise ValueError("name can't be empty")
        self.__name = value
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    def to_dict(self):
        """Return a dictionary representation of an amenity"""
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
        }
