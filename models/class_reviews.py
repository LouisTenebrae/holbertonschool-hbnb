import uuid
from datetime import datetime
from persistence.DataManager import DataManager


class Review(DataManager):
    """"Review class"""

    def __init__(self, text, rating, user_id, place_id):
        self.__id = str(uuid.uuid4())  # Genera un ID único
        self.__text = text
        self.__rating = rating
        self.__place_id = place_id
        self.__user_id = user_id
        self.__created = datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated = self.__created

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def created(self):
        return self.__created

    @property
    def updated(self):
        return self.__updated

    @property
    def text(self):
        return self.__text

    @property
    def rating(self):
        return self.__rating

    @property
    def place_id(self):
        return self.__place_id

    @property
    def user_id(self):
        return self.__user_id

    @rating.setter
    def rating(self, value):
        if type(value) is not int:
            raise TypeError("rating must be an integer")
        if value < 0 or value > 5:
            raise ValueError("rating must be between 0 and 5")
        self.__rating = value
        self.__updated = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @text.setter
    def text(self, value):
        if type(value) is not str:
            raise TypeError("text must be a string")
        if len(value) == 0:
            raise ValueError("text cannot be empty")
        self.__text = value
        self.__updated = datetime.now().strftime("%b/%d/%y %I:%M %p")

    def to_dict(self):
        """Returns a dictionary representation of a review"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "place_id": self.place_id,
            "text": self.text,
            "rating": self.rating,
            "created_at": self.created,
            "updated_at": self.updated,
        }
