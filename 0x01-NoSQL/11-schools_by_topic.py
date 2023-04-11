#!/usr/bin/env python3
'''Demonstrate Python and mongoDB
'''

def schools_by_topic(mongo_collection, topic):
    '''returns the list of school having a specific topic
    '''
    return [school for school in mongo_collection.find({"topics": topic })]

if __name__ == "__main__":
    schools_by_topic(mongo_collection, topic)
