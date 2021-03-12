import json
from bson.json_util import dumps


def read(db, n):
    col = db['posts']
    cursor = col.find()
    acc = []
    for index, doc in enumerate(cursor):
        if index == n:
            break
        acc.append(dumps(doc))

    return acc
