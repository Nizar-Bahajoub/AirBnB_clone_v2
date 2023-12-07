#!/usr/bin/python3
"""
amenity module
"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class
    """

    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

        def __init__(self, *args, **kwargs):
            """Overriding constructor"""
            super().__init__(*args, **kwargs)
