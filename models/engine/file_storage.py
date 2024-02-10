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

    # Abstracted storage engine representation with attributes:
    # __file_path (file name for saving objects) and __objects (dictionary storing instantiated objects).

    __file_path = "file.json"
    __objects = {}

    def all(self):
        # return dict of all objects.
        return FileStorage.__objects

    def new(self, obj):
        # set new object to objects dictionary.
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        # serialize objects dictionary to JSON file.
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        # deserialize JSON file to objects dict.
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
