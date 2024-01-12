#!/usr/bin/env python3
"""this python script provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    print(f"{logs_collection.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    to_find = [{'method': 'GET'}, {'path': '/status'}]
    print(f"{logs_collection.count_documents({'$and': to_find})} status check")
