#!/usr/bin/python3
"""
review module
"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Review class
    """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
