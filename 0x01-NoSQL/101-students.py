#!/usr/bin/env python3
'''function that returns all students sorted by average score'''
from pymongo import MongoClient


def top_students(mongo_collection):
    '''returns stidents sorted by avg score'''
    pipeline = [
        {
            '$project': {
                'name': 1,
                'averageScore': { '$avg': '$topics.score' }
            }
        },
        {
            '$sort': { 'averageScore': -1 }
        }
    ]
    result = mongo_collection.aggregate(pipeline)

    return list(result)
