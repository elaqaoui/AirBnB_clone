#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    square_brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if square_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            token_parse = split(arg[:square_brackets.span()[0]])
            return_list = [i.strip(",") for i in token_parse]
            return_list.append(square_brackets.group())
            return return_list
    else:
        token_parse = split(arg[:curly_braces.span()[0]])
        return_list = [i.strip(",") for i in token_parse]
        return_list.append(curly_braces.group())
        return return_list


class HBNBCommand(cmd.Cmd):
    """Defines the alx command interpreter for the AirBnB console.
    the Attributes:
        prompt (str):
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """dont make anything when an empty line is entered."""
        pass

    def default(self, arg):
        """Default behavior for cmd module."""
        arguments_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        pattern_match = re.search(r"\.", arg)
        if pattern_match is not None:
            argl = [arg[:pattern_match.span()[0]], arg[pattern_match.span()[1]:]]
            pattern_match = re.search(r"\((.*?)\)", argl[1])
            if pattern_match is not None:
                command = [argl[1][:pattern_match.span()[0]], pattern_match.group()[1:-1]]
                if command[0] in arguments_dict.keys():
                    function_call = "{} {}".format(argl[0], command[1])
                    return arguments_dict[command[0]](function_call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        serialized_data = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in serialized_data:
            print("** no instance found **")
        else:
            print(serialized_data["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        serialized_data = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in serialized_data.keys():
            print("** no instance found **")
        else:
            del serialized_data["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    object_list.append(obj.__str__())
                elif len(argl) == 0:
                    object_list.append(obj.__str__())
            print(object_list)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        serialized_data = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in serialized_data.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = serialized_data["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = serialized_data["{}.{}".format(argl[0], argl[1])]
            for kv, val in eval(argl[2]).items():
                if (kv in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[kv]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[kv])
                    obj.__dict__[kv] = valtype(val)
                else:
                    obj.__dict__[kv] = val
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
