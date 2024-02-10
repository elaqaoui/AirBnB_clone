#!/usr/bin/env python3
# Program named console.py that serves as the entry point for the command interpreter.

import cmd
import os
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
# Class to manage the console and handle all commands built for the project.
    prompt = '(hbnb)'
    TRU_classes = ['BaseModel', 'User', 'Amenity', 'Review', 'State', 'City',
                     'Place']

    ERROR_CLASS_NAME_MISSING = '** class name missing **'
    ERROR_CLASS_NOT_EXIST = "** class doesn't exist **"
    ERROR_ID_MISSING = "** instance id missing **"
    ERROR_ID_NOT_EXIST = "** no instance found **"
    ERROR_ATTRI_NAME_MISSING = "** attribute name missing **"
    ERROR_ATTRI_VALUE_MISSING= "** value missing **"

    # Helper function to modify the command-line interpreter. This function
    # handles and reorders the input of the console to allow the functions to
    # work with a formatted command line.
    def terminal_upd_line_split(self, command, class_name):

        if command.find("(") != -1:
            attr_name = ''
            value = ''

            cmd_args_split = command.split('(')
            command = cmd_args_split[0]
            cmd_args_split[1] = cmd_args_split[1].replace(')', '')
            cmd_args_split[1] = cmd_args_split[1].replace('"', '')
            args = cmd_args_split[1].split(',')
            id_number = args[0].strip(" ")
            if len(args) > 1:
                attr_name = args[1].strip(" ")
            if len(args) > 2:
                value = args[2].strip(" ")
            return '{} {} {} {} "{}"'.format(command, class_name, id_number,
                                             attr_name, value)

        elif class_name in HBNBCommand.TRU_classes:
            return "{} {}".format(command, class_name)

    def onecmd(self, line: str) -> bool:
# Updating the command-line interpreter to allow this usage:
# <class name>.<command>() or <class name>.<command>("args")

        command_line_split = line.split(".")
        # Class.command
        if len(command_line_split) > 1:
            class_name = command_line_split[0]
            command = command_line_split[1].replace('()', '')
            # parameters
            line = self.terminal_upd_line_split(command, class_name)

        return super().onecmd(line)

    def Argument_lent_upd(self, arg):
    # Validates if the command receives the class_name argument.
        if len(arg) == 0:
            print(HBNBCommand.ERROR_CLASS_NAME_MISSING)
            return False
        return True

    def affecte_extr_classes(self, arg):
        # Validates if the specified argument contains a valid class name.

        args = arg.split(' ')
        class_name = args[0]
        if class_name not in HBNBCommand.TRU_classes:
            print(HBNBCommand.ERROR_CLASS_NOT_EXIST)
            return False
        return class_name

    def affect_extracting_more_id(self, arg):
        # Validates the presence of an 'id_number' argument in the command.
        args = arg.split(' ')
        if len(args) < 2:
            print(HBNBCommand.ERROR_ID_MISSING)
            return False
        id_number = args[1]
        return id_number

    def extract_working_attribute(self, arg):
        #Validates the presence of an attribute argument in the command.
        args = arg.split(' ')
        if len(args) < 3:
            print(HBNBCommand.ERROR_ATTRI_NAME_MISSING)
            return False
        attribute = args[2]
        return attribute

    def extract_working_attribute_valeur(self, arg):
        #Validates the presence of an attribute value in the command.
        args = arg.split(' ')
        if len(args) < 4:
            print(HBNBCommand.ERROR_ATTRI_VALUE_MISSING)
            return False
        attr_value = args[3]
        return attr_value

    def do_EOF(self, arg):
        # Quits with a new line <end of file>
        # Usage: Ctrl + d

        print()
        return True

    def emptyline(self):
        #check for emptylines
        pass

    def do_quit(self, arg):
        # Exits the program to quit the console
        return True

    def do_create(self, arg):
        # Creates new elements Usage: create <class_name> or <class_name>.create().
        if not self.Argument_lent_upd(arg):
            return

        class_name = self.affecte_extr_classes(arg)
        if not class_name:
            return

        storage.create(class_name)

    def do_show(self, arg):
       # Shows an element by id_number Usage: show <class_name> <id> or <class_name>.show("<id>")
        if not self.Argument_lent_upd(arg):
            return

        class_name = self.affecte_extr_classes(arg)
        if not class_name:
            return

        id_number = self.affect_extracting_more_id(arg)
        if not id_number:
            return
        objects = storage.all()
        keys = "{}.{}".format(class_name, id_number)
        try:
            print(objects[keys])
        except:
            print(HBNBCommand.ERROR_ID_NOT_EXIST)

    def do_destroy(self, arg):
        # Deletes elements in storage Usage: destroy <class_name> <id> or <class_name>.destroy("<id>").
        if not self.Argument_lent_upd(arg):
            return

        class_name = self.affecte_extr_classes(arg)
        if not class_name:
            return

        id_number = self.affect_extracting_more_id(arg)
        if not id_number:
            return

        objects = storage.all()
        keys = "{}.{}".format(class_name, id_number)

        try:
            del objects[keys]
            storage.save()
        except:
            print(HBNBCommand.ID_missing)

    def do_all(self, arg):
        # Prints all elements in storage by class name.
        class_name = None
        if len(arg) > 0:
            class_name = self.affecte_extr_classes(arg)
            if not class_name:
                return
            # filter data
        storage.print(class_name)

    def do_update(self, arg):
    # Updates info in storage
    # Usage: update <class_name> <id> <attribute_name> <attribute_value>
    # or <class_name>.update("<id>", "<attribute_name>", "<attribute_value>")

        if not self.Argument_lent_upd(arg):
            return
        class_name = self.affecte_extr_classes(arg)
        if not class_name:
            return
        id_number = self.affect_extracting_more_id(arg)
        if not id_number:
            return

        attribute = self.extract_working_attribute(arg)
        if not attribute:
            return
        attr_value = self.extract_working_attribute_valeur(arg)
        if not attr_value:
            return
        try:
            objects = storage.all()
            keys = "{}.{}".format(class_name, id_number)
            obj = objects[keys]
        except:
            print(HBNBCommand.ID_missing)
            return

        # obj[attribute] = attr_value
        attr_value = attr_value.strip('"')

        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except:
                pass

        setattr(obj, attribute, attr_value)
        obj.save()

    def do_clear(self, _):
       # Clears the screen.
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def do_count(self, arg):
       # Counts the number of elements in storage.
        if not self.Argument_lent_upd(arg):
            return
        class_name = self.affecte_extr_classes(arg)
        if not class_name:
            return

        filtered_class_list = storage.filter_elements_by_class(class_name)
        print(len(filtered_class_list))

if __name__ == '__main__':
    HBNBCommand().cmdloop()

