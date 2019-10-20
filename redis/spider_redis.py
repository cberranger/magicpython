#!/usr/bin/env python3
# -*-coding : utf-8 -*-
import redis
from RedisUtils import getRedisConnectionWithPool
r = getRedisConnectionWithPool()
r.set('hello', 'haha')
a = r.get('hello')
print(a)
