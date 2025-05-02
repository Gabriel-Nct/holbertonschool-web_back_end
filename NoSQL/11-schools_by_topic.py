#!/usr/bin/env python3
"""
Module that defines a function to find schools by a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the specified topic.
    Args:
        mongo_collection: The pymongo collection object
        where the documents are stored.
        topic (str): The topic to search for in the school's document.
    Returns:
        list: A list of schools that have the specified topic
        in their 'topics' field.
    """
    return mongo_collection.find({"topics": topic})
