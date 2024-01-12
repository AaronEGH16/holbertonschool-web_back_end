#!/usr/bin/env python3
"""
this module contains a insert_school function definition
"""


def insert_school(mongo_collection, **kwargs):
    """
    this function get a MongoDB collection and all values to
    insert a new collection element, and return the new element id
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
