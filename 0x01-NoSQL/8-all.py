#!/usr/bin/env python3
'''Demonstrate Python and mongoDB
'''


def list_all(mongo_collection):
    '''Documents in Python
        return: [] or all documents
    '''
    empty_list = []
    if mongo_collection.find():
        return mongo_collection.find()
    return empty_list

if __name__ == "__main__":
    list_all(mongo_collection)
