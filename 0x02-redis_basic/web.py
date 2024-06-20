#!/usr/bin/env python3
'''
Track how many times a particular URL was accessed
'''
import redis
import requests

redis_client = redis.Redis()


def get_page(url: str) -> str:
    '''"A web scraper"'''
    if not url or len(url.strip()) == 0:
        return ''

    # redis_client = redis.Redis()
    count_key = f'count:{url}'
    redis_client.incr(count_key)

    cached_page = redis_client.get(url)
    if cached_page:
        return cached_page.decode('utf-8')

    response = requests.get(url)
    # htm_content = response.text # Same thing apparently
    html_content = response.content.decode('utf-8')

    redis_client.setex(url, 10, html_content)

    return html_content
