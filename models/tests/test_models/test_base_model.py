#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """
    def test_init(self):
        """Test init"""
        my_model = ModelBase()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.create_at)
        self.assertIsNotNone(my_model.update_at)

    def test_save(seelf):
        """Test to save Method"""
        my_model = BaseModel()

        init_update = my_model.update_at
        current_update = my_model.save()

        self.assertNotEqual(init_update, current_update)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"] , my_model.created_at.isoformat())

    def test_str(self):
        """
        Test for string representation
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
