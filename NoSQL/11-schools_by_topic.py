#!/usr/bin/env python3
"""
this module contains a definition of schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """
    This function returns a list of all the elements of a
    "MongoDB collection" (passed by arg) whose "topic" value contains
    the "topic" argument
    """
    return list(mongo_collection.find({"topics": {"$in": [topic]}}))
