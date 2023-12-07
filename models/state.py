#!/usr/bin/python3
"""
state  module
"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State class
    """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade='all, delete')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """FileStorage relationship between State and City"""
        my_list = []
        for obj in models.storage.all(City).values():
            if obj.state_id == self.id:
                my_list.append(obj)
        return (my_list)
