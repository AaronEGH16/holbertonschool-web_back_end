#!/usr/bin/env python3
"""
this module contains a list_all function definition
"""
from typing import List
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List:
    """
    this function get a MongoDB collection
    and return a list of all collection elements
    """
    return list(doc for doc in mongo_collection.find())
