#!/usr/bin/python3
# This is a module test from BaseModel class and your methods.
import unittest
from models.user import User


class TestUser(unittest.TestCase):
   # this class test user class and your behavior
    def setUp (self):
        self.user = User()

    def test_creation_success(self):
        # this test validate that creation proccess was correct.
        data = {'id' : 3,
            'fist_name' : 'Betty',
            'last_name':'alx',
            'password':'root',
            'email':'aibnb@mail.com',
            }

        self.user = User(**data)
        self.assertEqual(self.user.id, 3)
        self.assertEqual(self.user.first_name, 'Betty')
        self.assertEqual(self.user.first_name, 'alx')
        self.assertEqual(self.user.password, 'root')
        self.assertEqual(self.user.email, 'aibnb@mail.com')
