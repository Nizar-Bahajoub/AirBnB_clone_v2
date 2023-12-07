#!/usr/bin/python3
"""
DBStorage engine
"""
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import InvalidRequestError


classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    """DataBase Storgae"""
    __engine = None
    __session = None
    __scoped_session = None
    __objects = {}

    def __init__(self):
        """Initialization method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        self.__objects.clear()
        result = {}
        classes_to_query = []
        if cls:
            if cls in classes.values():
                classes_to_query.append(cls)
            else:
                return result
        else:
            classes_to_query = classes.values()

        for class_to_query in classes_to_query:
            objects = self.__session.query(class_to_query).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                result[key] = obj
        return result

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__scoped_session = Session
        self.__session = Session()

    def close(self):
        """New method"""
        self.__session.close()
