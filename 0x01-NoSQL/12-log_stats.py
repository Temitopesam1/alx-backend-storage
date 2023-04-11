#!/usr/bin/env python3
'''Demonstrate Python and mongoDB
'''

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    print(f'{client.logs.nginx.count_documents()} logs')
    print('Methods:')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        print(f'\tmethod {method}: {client.logs.nginx.count_documents({'method': method})}')

    print(f'{client.logs.nginx.count_documents({'method': 'GET', 'path': '/status'})} status check')

