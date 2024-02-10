#!/usr/bin/python3
# amenity module test
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
# this class test Amenity class and your behavior

    def setUp (self):
        self.amenity = Amenity()

    def test_creation_success(self):
        # this test validate that creation proccess was correct.
        self.assertEqual(self.amenity.name, '')