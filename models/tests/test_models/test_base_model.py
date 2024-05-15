i#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.basemodel import BaseModel

class TestBaseModel_instantiation(unittest.TestCase):
    """Unittest of BaseModel instantiation of the BaseModel"""
    def test_args_instantiation(self):
        self..assertEqual(Basemodel, type(BaseModel()))

    def test_new_instance_stored_in_object(self):
        self.assertin(BaseModel(), models.storage.all().value())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_create_at_is_public_datetime(self):
        self.assertEqual(create_at, type(BaseModel().create_at))

    def test_update_at_is_public_datetime(self):
        self.assertEqual(update_at, type(BaseModel().update_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

