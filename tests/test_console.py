#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
import os
import sys
from console import HBNBCommand
from io import StringIO

class TestHBNBCommand(unittest.TestCase):
    # This class tests the 'HBNBCommand' class and its behavior.

    def setUp (self) -> None:
        return super().setUp ()

    def test_simple_bnb(self, testfunc, arg, exeption):
    # Auxiliary function to test some commands of the console.
        capt_output = StringIO()
        sys.stdout = capt_output
        testfunc(arg)
        output = capt_output.getvalue()
        self.assertEqual(output, exeption + '\n')
        return output

    def FailToCreate_test(self):
   # Testing the 'create' command of the console - focusing on error messages.
        try:
            os.remove('file.json')
        except:
            pass
        cmd = HBNBCommand()

        self.test_simple_bnb(cmd.do_create, '', HBNBCommand.ERROR_CLASS_NAME_MISSING)
        self.test_simple_bnb(cmd.do_create, 'myModel', HBNBCommand.CLASS_ERR)

    # Test function for the 'create' command - positive scenario.
    # def creation_done(self):
    #     cmd = HBNBCommand()
    #     out = self.test_simple_bnb(cmd.do_create, 'BaseModel', '')