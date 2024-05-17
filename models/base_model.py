#!/usr/bin/python3
"""Define a BaseModel class"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represent BaseModel"""
    def __init__(self, *args, **kwargs):
        """ Construct """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
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
