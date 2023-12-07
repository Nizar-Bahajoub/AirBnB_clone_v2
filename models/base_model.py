#!/usr/bin/python3
"""
base_model module
"""
from os import getenv
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime


if getenv('HBNB_TYPE_STORAGE') == "db":
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """BaseModel Class"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        id = Column(String(60),
                    nullable=False,
                    primary_key=True)
        created_at = Column(DateTime,
                            nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime,
                            nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    elif key == 'id':
                        self.id = str(uuid.uuid4())
                    else:
                        setattr(self, key, value)


    def __str__(self):
        """String representation of BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of all the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        return (my_dict)

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
