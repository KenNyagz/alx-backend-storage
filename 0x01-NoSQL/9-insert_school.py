#!/usr/bin/env python3
'''Python function that inserts a new doc in a collection based on kwargs'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new docs in a collection based on kwargs'''
    inserted_doc = mongo_collection.insert_one(kwargs)
    return inserted_doc.inserted_id
