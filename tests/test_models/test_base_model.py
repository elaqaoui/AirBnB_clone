#!/usr/bin/env python3

# This is a module test for the BaseModel class and its methods.

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import models

class TestBaseModelInitialization(unittest.TestCase):

    # Unittests for the initialization of the BaseModel class.
    def test_no_args_initialization(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_pub_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_two_models_ids_unique(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_creation_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_check_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_time_created(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_models_time_updated(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_kwargs_args(self):
        t = datetime.today()
        t_form = t.isoformat()
        mod = BaseModel("12", id="345", created_at=t_form, updated_at=t)
        self.assertEqual(mod.id, "345")
        self.assertEqual(mod.created_at, t)
        self.assertEqual(mod.updated_at, t)

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_args_non(self):
        mod = BaseModel(None)
        self.assertNotIn(None, mod.__dict__.values())


class TestBaseModelSave(unittest.TestCase):
        # Unittests for the save method of the BaseModel class.
        def test_save_method_updated_at(self):
                mod = BaseModel()
                sleep(0.05)
                updated_at1 = mod.updated_at
                mod.save()
                self.assertLess(updated_at1, mod.updated_at)

        def test_save2_method(self):
                mod = BaseModel()
                sleep(0.05)
                updated1 = mod.updated_at
                mod.save()
                update2 = mod.updated_at
                self.assertLess(updated1, update2)
                sleep(0.05)
                mod.save()
                self.assertLess(update2, mod.update_at)

class TestBaseModelToDict(unittest.TestCase):
        # unittests for to_dict method of BaseModel class.
        def test_dict_typ(self):
                mod = BaseModel()
                self.assertTrue(dict, type(mod.to_dict()))

        def test_dict_kys(self):
                mod = BaseModel()
                base_dict = mod.to_dict()
                self.assertIn('id', base_dict)
                self.assertIn('created_at', base_dict)
                self.assertIn('updated_at', base_dict)
                self.assertIn('__class__', base_dict)

        def test_dict_general(self):
                t = datetime.today()
                mod = BaseModel()
                mod.id = '00'
                mod.created_at = mod.updated_at = t
                base_dict = {
                        'id': '00',
                        '__class__': 'BaseModel',
                        'created_at': t.isoformat(),
                        'updated_at': t.isoformat()
                        }
                self.assertDictEqual(mod.to_dict(), base_dict)


if __name__ == "__main__":
        unittest.main()
