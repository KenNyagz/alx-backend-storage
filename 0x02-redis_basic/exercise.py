#!/usr/bin/env python3
'''
Class for redis databases and the methods involved in managing the data
'''
import redis
from typing import Union
import uuid


class Cache:
    '''Class for defining redis cache objects'''
    def __init__(self):
        '''Initialize Redis client and flush the database'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Generate random key and save the data to that key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        #self._redis.set(key, str(data).encode())
        return key
