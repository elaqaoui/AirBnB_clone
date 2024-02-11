#!/usr/bin/python3
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    # base model instantiation tests for BaseModel.
    def test_instantiation_without_arguments(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_instance_stored_in_object_manager(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_public_id_is_string(self):
        self.assertEqual(str, type(Amenity().id))

    def test_public_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_class_attribute(self):
        a1 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", a1.__dict__)

    def test_nom_class_istribute(self):
        a2 = Amenity()
        a3 = Amenity()
        self.assertNotEqual(a2.id, a3.id)

    def test_different_created_at_for_two_amenities(self):
        a2 = Amenity()
        sleep(0.05)
        a3 = Amenity()
        self.assertLess(a2.created_at, a3.created_at)

    def test_different_updated_at_for_two_amenities(self):
        a2 = Amenity()
        sleep(0.05)
        a3 = Amenity()
        self.assertLess(a2.updated_at, a3.updated_at)

    def test_str_reprisent(self):
        dt = datetime.today()
        time_repr = repr(dt)
        a1 = Amenity()
        a1.id = "123456"
        a1.created_at = a1.updated_at = dt
        a_string = a1.__str__()
        self.assertIn("[Amenity] (123456)", a_string)
        self.assertIn("'id': '123456'", a_string)
        self.assertIn("'created_at': " + time_repr, a_string)
        self.assertIn("'updated_at': " + time_repr, a_string)

    def test_args_not_used(self):
        a1 = Amenity(None)
        self.assertNotIn(None, a1.__dict__.values())

    def test_instantiation_with_keyword_arguments(self):
        # tests if the object is stored in the object manager
        dt = datetime.today()
        time_iso = dt.isoformat()
        a1 = Amenity(id="345", created_at=time_iso, updated_at=time_iso)
        self.assertEqual(a1.id, "345")
        self.assertEqual(a1.created_at, dt)
        self.assertEqual(a1.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    # tests the save method
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_first_save(self):
        a1 = Amenity()
        sleep(0.05)
        first_updated_at = a1.updated_at
        a1.save()
        self.assertLess(first_updated_at, a1.updated_at)

    def test_two_saves(self):
        a1 = Amenity()
        sleep(0.05)
        first_updated_at = a1.updated_at
        a1.save()
        second_updated_at = a1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        a1.save()
        self.assertLess(second_updated_at, a1.updated_at)

    def test_save_with_arg(self):
        a1 = Amenity()
        with self.assertRaises(TypeError):
            a1.save(None)

    def test_save_updates_file(self):
        a1 = Amenity()
        a1.save()
        a_id = "Amenity." + a1.id
        with open("file.json", "r") as f:
            self.assertIn(a_id, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    # amenity to dictionary tests for Amenity.
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        a1 = Amenity()
        self.assertIn("id", a1.to_dict())
        self.assertIn("created_at", a1.to_dict())
        self.assertIn("updated_at", a1.to_dict())
        self.assertIn("__class__", a1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        a1 = Amenity()
        a1.middle_name = "Holberton"
        a1.my_number = 98
        self.assertEqual("Holberton", a1.middle_name)
        self.assertIn("my_number", a1.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        a1 = Amenity()
        a_dict = a1.to_dict()
        self.assertEqual(str, type(a_dict["id"]))
        self.assertEqual(str, type(a_dict["created_at"]))
        self.assertEqual(str, type(a_dict["updated_at"]))

    def test_dictio_to_output(self):
        dt = datetime.today()
        a1 = Amenity()
        a1.id = "123456"
        a1.created_at = a1.updated_at = dt
        t_dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(a1.to_dict(), t_dict)

    def test_const_to_diction(self):
        a1 = Amenity()
        self.assertNotEqual(a1.to_dict(), a1.__dict__)

    def test_to_dict_with_arg(self):
        a1 = Amenity()
        with self.assertRaises(TypeError):
            a1.to_dict(None)


if __name__ == "__main__":
    unittest.main()
