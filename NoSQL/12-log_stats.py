#!/usr/bin/env python3
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient()

# Connect to the logs database and the nginx collection
db = client.logs
nginx_collection = db.nginx

# Count the total number of documents in the collection
total_logs = nginx_collection.count_documents({})

# Count the number of documents for each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: nginx_collection.count_documents({"method": method}) for method in methods}

# Count the number of documents where method=GET and path=/status
status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})

# Output the results in the specified format
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
