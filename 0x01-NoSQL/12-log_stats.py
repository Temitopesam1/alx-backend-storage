#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    count_logs = client.logs.nginx.count_documents({})
    print(f'{count_logs} logs')

    print('Methods:')
    for method in methods:
        count_method = client.logs.nginx.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')

    check = db_nginx.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{check} status check')

