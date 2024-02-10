#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
#BaseModel class for other classes to inherit from.
    def __init__(self, *args, **kwargs):
        # Initialize the BaseModel instance.
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for kys, valu in kwargs.items():
                if kys == "created_at" or kys == "updated_at":
                    self.__dict__[kys] = datetime.strptime(valu, timeform)
                else:
                    self.__dict__[kys] = valu
        else:
            models.storage.new(self)

    def save(self):
        # update the updated_at attribute with the current datetime.
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
       # returns a dictionary containing all keys/values of __dict__.
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

