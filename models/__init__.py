#!/usr/bin/python3
"""__init__ magic method for models directory"""
from os import getenv
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


if getenv('HBNB_TYPE_STORAGE') == "db":

    storage = DBStorage()
    storage.reload()
else:

    storage = FileStorage()
    storage.reload()
