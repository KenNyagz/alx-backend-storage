#!/usr/bin/env python3
'''
Class for redis databases and the methods involved in managing the data
'''
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Counts number of times a method has been called'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''the decorator function'''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''add its input parameters to one list in redis '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''decorator function'''
        input_key = f'{method.__qualname__}:inputs'
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    '''Class for defining redis cache objects'''
    def __init__(self):
        '''Initialize Redis client and flush the database'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Generate random key and save the data to that key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        # self._redis.set(key, str(data).encode())
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, int, float, bytes]]:
        '''Reading from Redis and recovering original type'''
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> Optional[str]:
        '''Gets string version of data retrieved'''
        #return self.get(key, lambda x: x.decode('utf-8') if x else None)
        result = self.get(key, lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)
        return result if isinstance(result, str) else None

    def get_int(self, key: str) -> Optional[int]:
        '''gets integer version of data'''
        #return self.get(key, lambda x: int(x) if x else None)
        result = self.get(key, lambda x: int(x) if isinstance(x, (bytes, str)) else x)
        return result if isinstance(result, int) else None
