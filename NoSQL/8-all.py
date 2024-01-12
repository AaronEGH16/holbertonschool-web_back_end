#!/usr/bin/env python3
"""
this module contains a list_all function definition
"""


def list_all(mongo_collection):
    """
    this function get a MongoDB collection
    and return a list of all collection elements
    """
    return list(doc for doc in mongo_collection.find())
