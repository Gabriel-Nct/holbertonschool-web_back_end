#!/usr/bin/env python3
"""
Module that defines a function to insert
a new document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into the collection
    based on provided keyword arguments.

    Args:
        mongo_collection: The pymongo collection
        object where the document will be inserted.
        **kwargs: The fields and values for the new document.
    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
