#!/usr/bin/python3
"""
city module
"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    City class
    """

    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"))
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
