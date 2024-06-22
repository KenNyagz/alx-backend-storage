#!/usr/bin/env python3
'''provides some stats about Nginx logs stored in MongoDB'''
from pymongo import MongoClient


def main():
    '''Reads logs stored in mongodb and processes them'''
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f'{total_logs} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for method in methods:
        count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    get_status_count = collection.count_documents({'method': 'GET', 'path':
                                                   '/status'})
    print(f'{get_status_count} status check')

    pipeline = [
        {"group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = mongo_collection.aggregate(pipeline)
    print("IPs:")
    for ip in top_ips:
        print(f'\t{ip["_id"]}: {ip["count"]}')


if __name__ == "__main__":
    main()
