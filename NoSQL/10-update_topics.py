#!/usr/bin/env python3
"""
this module contains a definition of update_topics function
"""


def update_topics(mongo_collection, name, topics):
    """
    This function receives a collection from MongoDB, the name field
    and updates its field "topics" by topics arg
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
