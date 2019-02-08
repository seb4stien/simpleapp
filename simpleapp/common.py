import os
import redis
import time
import uuid


class Worker:
    def __init__(self):
        self.__id = uuid.uuid4()


class Backend:
    def __init__(self):
        host = os.environ.get("REDIS_SERVICE_HOST", "localhost")
        port = os.environ.get("REDIS_SERVICE_PORT", 6379)
        self.__redis = redis.Redis(host=host, port=port, decode_responses=True)

    def register(self, name):
        now = int(time.time())
        return self.__redis.hset("workers", name, now)

    def members(self):
        return self.__redis.hlen("workers")

    def increment(self, key):
        return self.__redis.incr(key)

    def get(self, key):
        return self.__redis.get(key)
