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

    check = client.logs.nginx.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{check} status check')
    print("IPs:")
    ips = client.logs.nginx.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    for ip in ips:
        print(f"\t{ip.get('ip')}: {ip.get('count')}")
