#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = FileStorage.__objects
        serialized_data = {obj: objects_dict[obj].to_dict() for obj in objects_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_data, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                serialized_data = json.load(f)
                for object_data in serialized_data.values():
                    class_type = object_data["__class__"]
                    del object_data["__class__"]
                    self.new(eval(class_type)(**object_data))
        except FileNotFoundError:
            return
