#!/usr/bin/python3
import uuid
from datetime import datetime
from .amenity import Amenity
from .class_reviews import Review
from persistence.DataManager import DataManager


class Places(DataManager):
    """Class that defines a list of Places for HBnB"""

    def __init__(self, name, description, address, latitude,
                 longitude, city_id, rooms, bathrooms, price, max_guests):
        self.__name = name
        self.__description = description
        self.__address = address
        self.__latitude = latitude
        self.__longitude = longitude
        self.__city_id = city_id
        self.__rooms = rooms
        self.__bathrooms = bathrooms
        self.__price = price
        self.__max_guests = max_guests
        self.__created_at = datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated_at = self.__created_at
        self.__id = str(uuid.uuid4())
        self.__host_id = None
        self.amenities = []
        self.reviews = []

    @property
    def review(self):
        """Getter for review"""
        return self.reviews

    def add_review(self, review):
        """Add a review to the list of reviews"""
        if not isinstance(review, Review):
            raise TypeError("review must be an instance of Review")
        self.reviews.append(review)
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def amenities(self):
        """Getter for amenities"""
        return self.amenities

    def add_amenity(self, amenity):
        """Add an amenity to the list of amenities"""
        if not isinstance(amenity, Amenity):
            raise TypeError("amenity must be an instance of Amenity")
        self.amenities.append(amenity)
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def host_name(self):
        """Getter for host_name"""
        return self.__host_name

    @host_name.setter
    def host_name(self, host_name):
        """Setter for host_name"""
        self.__host_name = host_name
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def host_id(self):
        """Getter for host_id"""
        return self.__host_id

    @host_id.setter
    def host_id(self, host_id):
        """Setter for host_id"""
        self.__host_id = host_id
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def id(self):
        """Getter for id"""
        return self.__id

    @property
    def created_at(self):
        """Getter for created_at"""
        return self.__created_at

    @property
    def updated_at(self):
        """Getter for updated_at"""
        return self.__updated_at

    @property
    def name(self):
        """Getter for name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Setter for name"""
        if type(name) is not str:
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be a string")
        self.__name = name
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def description(self):
        """Getter for description"""
        return self.__description

    @description.setter
    def description(self, description):
        """Setter for description"""
        if type(description) is not str:
            raise TypeError("Description must be a string")
        if len(description) == 0:
            raise ValueError("Description must be a string")
        self.__description = description
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def address(self):
        """Getter for address"""
        return self.__address

    @address.setter
    def address(self, address):
        """Setter for address"""
        if type(address) is not str:
            raise TypeError("Address must be a string")
        if len(address) == 0:
            raise ValueError("Address must be a string")
        self.__address = address
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def latitude(self):
        """Getter for latitude"""
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        """Setter for latitude"""
        if type(latitude) is not float:
            raise TypeError("Latitude must be a float")
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude must be between -90 and 90 degrees")
        self.__latitude = latitude
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def longitude(self):
        """Getter for longitude"""
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        """Setter for longitude"""
        if type(longitude) is not float:
            raise TypeError("Longitude must be a float")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude must be between -180 and 180 degrees")
        self.__longitude = longitude
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def city_id(self):
        """Getter for city"""
        return self.__city_id

    @city_id.setter
    def city_id(self, city_id):
        """Setter for city"""
        if not city_id or len(city_id) == 0:
            raise ValueError("City id must not be empty") 
        self.__city_id = city_id
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def rooms(self):
        """Getter for rooms"""
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        """Setter for rooms"""
        if type(rooms) is not int:
            raise TypeError("Rooms must be an integer")
        if rooms <= 0:
            raise ValueError("Rooms must be a more than 0")
        self.__rooms = rooms
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def bathrooms(self):
        """Getter for bathrooms"""
        return self.__bathrooms

    @bathrooms.setter
    def bathrooms(self, bathrooms):
        """Setter for bathrooms"""
        if type(bathrooms) is not int:
            raise TypeError("Bathrooms must be an integer")
        if bathrooms <= 0:
            raise ValueError("Bathrooms must be a more than 0")
        self.__bathrooms = bathrooms
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def price(self):
        """Getter for price"""
        return self.__price

    @price.setter
    def price(self, price):
        """Setter for price"""
        if type(price) is not int:
            raise TypeError("Price must be an integer")
        if price <= 0:
            raise ValueError("Price must be a more than 0")
        self.__price = price
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def max_guests(self):
        """Getter for max_guests"""
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests):
        """Setter for max_guests"""
        if type(max_guests) is not int:
            raise TypeError("Max guests must be an integer")
        if max_guests <= 0:
            raise ValueError("Max guests must be a more than 0")
        self.__max_guests = max_guests
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    def to_dict(self):
        """Convert place to dictionary"""
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
            "description": self.__description,
            "number_rooms": self.__rooms,
            "number_bathrooms": self.__bathrooms,
            "max_guests": self.__max_guests,
            "price_by_night": self.__price,
            "latitude": self.__latitude,
            "longitude": self.__longitude,
            "amenities": [amenity.to_dict() for amenity in self.amenities],
            "user_id": self.__host_id,
            "city_id": self.__city_id,
            "reviews": [review.to_dict() for review in self.reviews]
        }
