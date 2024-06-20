#!/usr/bin/env python3
'''

'''
import redis
import requests

redis_client = redis.Redis()


def get_page(url: str) -> str:
    '''A web scraper'''
    count_key = f'count:{url}'
    redis_client.incr(count_key)

    cached_page = redis_client.get(url)
    if cached_page:
        return cached_page.decode('utf-8')

    response = requests.get(url)
    html_content = response.text

    redis_client.setex(url, 10, html_content)

    return html_content
