#!/usr/bin/python3
# test_file_storage - Test FileStorage class
from models.engine.file_storage import FileStorage
import unittest
from models.engine.file_storage import BaseModel


class testing_file_storage(unittest.TestCase):

    def test_instantiation(self):
        # make sure that the creation process was correct.
        self.assertEqual(type(FileStorage()), FileStorage)

    def setUp (self):
        # init the storage class
        self.storage = FileStorage()

    def test_creation_success(self):
        # make sure that the creation process was correct.
        self.assertEqual(self.storage.save(), None)
