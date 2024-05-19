#!/usr/bin/python3
from models.base_model import BaseModel

class user(BaseModel):
    """user inherit a BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
