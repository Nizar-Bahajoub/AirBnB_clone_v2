#!/usr/bin/python3
"""
place module
"""
from os import getenv
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """
    Place class
    """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True, default=None)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="all, delete")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []


        def __init__(self, *args, **kwargs):
            """Overriding constructor"""
            super().__init__(*args, **kwargs)

        @property
        def reviews(self):
            """returns a list or reviews"""
            my_list = []
            for obj in models.storage.all(Place).values():
                if obj.place_id == self.id:
                    my_list.append(obj)
            return (my_list)

        @property
        def amenities(self):
            """ returns the list of Amenity instances based on the
            attribute amenity_ids that contains all 
            Amenity.id linked to the Place
            """
            amenity_instances = models.storage.all(Amenity)
            my_list = []
            for obj in amenity_instances:
                if obj.id in self.amenity_ids:
                    my_list.append(obj)
            return (my_list)

        @amenities.setter
        def amenities(self, amenity_obj):
            if isinstance(amenity_obj, Amenity) and amenity_obj not in self.amenity_ids:
                self.amenity_ids.append(amenity_obj.id)
