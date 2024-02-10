#!/usr/bin/env python3
import json
import importlib
import re

class FileStorage:
   # FileStorage: Abstracted file storage with methods for managing and serializing objects to a JSON file.
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        # returns the dictionary objects
        return FileStorage.__objects

    def new(self, obj):
       # Creates and saves a new instance of a specific class into the file storage.

        key_name = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_name] = obj

    def save(self):
      # Saves instances of all classes into a .json file using the JSON string format.

        content = self._objects_json()

        with open(FileStorage.__file_path, 'w') as file:
            file.write(content)

    def reload(self):
        # Deserializes the JSON file to __objects if it exists; otherwise, does nothing.

        file_data = self.deserialize_json_to_objects()

        if not file_data:
            return

        for k, value in file_data.items():
            class_name = value["__class__"]
            FileStorage.__objects[k] = self.instantiate_classe(class_name, value)

    def create(self, class_name):
         # Auxiliar function to create new instances of an specific class

        my_model = self.instantiate_classe(class_name)
        my_model.save()
        print(my_model.id)

    def instantiate_classe(self, class_name, data=None):
       # Chooses the correct class for an instance, facilitating instance creation, to_dict function usage, and saving into the JSON file.
        module_name = self.conv_to_snake_case(class_name)
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        if data:
            return class_(**data)
        else:
            return class_()

    def print(self, class_name=None):
        """ print all elements in storage and filter by class_name"""
        print(self.filter_elements_by_class(class_name))

    def filter_elements_by_class(self, class_name):
        """Auxiliar function to print or show the instances of an specific
        type of class.
        """
        if not class_name:
            return self.dict_list_conv()

        filtered = []
        for k, value in self.all().items():
            split_key = k.split('.')
            if split_key[0] == class_name:
                filtered.append(str(value))
        return filtered

    def dict_list_conv(self):
        """ take a dictionary and transform this to list
            with objects cast to str"""
        data_list = []
        for _, value in self.all().items():
            data_list.append(str(value))
        return data_list

    def _objects_json(self):
        """
        BaseModel->to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'>
        """
        objects = {}
        for keys, obj in self.all().items():
            objects[keys] = obj.to_dict()

        return str(json.dumps(objects))

    def deserialize_json_to_objects(self):
        "File -> str -> JSON load -> dict -> BaseModel"
        try:
            with open(FileStorage.__file_path) as file:
                return json.load(file)
        except:
            pass

    def conv_to_snake_case(self, text):
        """ Transform text to snake case """
        module_name = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
        return "models.{}".format(module_name)
