"""
Common classes
"""

# stdlib
import os
import time
import uuid

# requirements
import redis


class Worker:
    def __init__(self):
        self.__id = uuid.uuid4()


class Backend:
    def __init__(self):
        url = os.environ.get("SAPP_REDIS_URL")

        if not url:
            raise RuntimeError("You must define SAPP_REDIS_URL")

        self.__redis = redis.Redis.from_url(url, decode_responses=True)

    def register(self, name):
        now = int(time.time())
        return self.__redis.hset("workers", name, now)

    def members(self):
        return self.__redis.hlen("workers")

    def increment(self, key):
        return self.__redis.incr(key)

    def get(self, key):
        return self.__redis.get(key)
