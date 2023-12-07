#!/usr/bin/python3
"""
file_storage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel,
                  "User": User,
                  "Place": Place,
                  "State": State,
                  "City": City,
                  "Amenity": Amenity,
                  "Review": Review
                  }

    def all(self, cls=None):
        """returns the dictionary"""
        if cls:
            my_dict = {}
            for key, value in FileStorage.__objects.items():
                class_name = key.split('.')[0]
                if cls.__name__ == class_name:
                    my_dict[key] = value
            return (my_dict)
        else:
            return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj"""
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """serializes __objects to JSON file"""
        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized, file)

    def reload(self):
        """Dokeserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                deserialized = json.load(file)
                for key, value in deserialized.items():
                    class_name = value['__class__']
                    obj = self.class_dict[class_name](**value)
                    self.__class__.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside"""
        if obj:
            obj_name = obj.__class__.__name__ + '.' + obj.id
            if obj_name in FileStorage.__objects:
                del FileStorage.__objects[obj_name]
            self.save()
        else:
            return

    def close(self):
        """Deserializing JSON file to objects"""
        self.reload()
