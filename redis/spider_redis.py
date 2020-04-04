#!/usr/bin/env python3
# -*-coding : utf-8 -*-
import redis
from RedisUtils import getRedisConnectionWithPool
from distributedLock import Lock,tryLock,releaseLock

if __name__ == "__main__":
    r = getRedisConnectionWithPool()
    lock = Lock("lock1", "lock1value")
    if tryLock(r, lock):
        print("yes")
    else:
        print("false")
