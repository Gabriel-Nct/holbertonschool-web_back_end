#!/usr/bin/env python3
"""
Module that defines a function to update
the topics of a school document in MongoDB.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on its name.
    Args:
        mongo_collection: The pymongo
        collection object where the document is located.
        name (str): The name of the school
        whose topics are to be updated.
        topics (list): The list of topics
    Returns:
        None
    """
    mongo_collection.update_many(
      {"name": name},
      {"$set": {"topics": topics}}
    )
