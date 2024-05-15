#!/usr/bin/python3
"""Define a BaseModel class"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represent BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialize the new BaseModel.

        Args:
            *args(any): any arguments
            *kwargs(dict): key/value pairs of attributes.
        """
        met = "%y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "create_at" or key == "update_at":
                    self.__dict__[key] = datetime.strptime(value, met)
                else
                    self.__dict__[key] = value
        else
            models.storage.new(self)

    def __str__(self):
        """Represent BaseModel in string"""
        nom = self.__class__.__name__
        return ("{} {} {}".format(nom, self.id, self.__dict__))
    def save(self):
        self.update_at = datetime.now()
        models.storage.save()
    @property
    def __dict__(self):
        tdict = self.__dict__.copy()
        tdict["create_at"] = self.create_at.isoformat()
        tdict["update_at"] = self.update_at.isoformat()
        tdict["__class__"] = self.__class__.__name__
        return tdict
