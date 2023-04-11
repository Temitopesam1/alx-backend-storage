#!/usr/bin/env python3
'''Demonstrate Python and mongoDB
'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document in a collection based on kwargs
        return: new _id
    '''
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id

if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
