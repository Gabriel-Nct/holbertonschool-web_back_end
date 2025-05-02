#!/usr/bin/env python3
"""
Module that provides stats about Nginx logs.
"""
from pymongo import MongoClient
"""
importing MongoClient from pymongo
"""


def log_stats():
    """Displays stats about the Nginx logs."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})

    print(f"{total_logs} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check_count = nginx_collection.count_documents({"method": "GET",
                                                           "path": "/status"})

    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
