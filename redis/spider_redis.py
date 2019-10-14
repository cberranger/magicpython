#!/usr/bin/env python3
# -*-coding : utf-8 -*-
import redis
ip = "localhost"
port = 6379
password =

r = redis.Redis(host=ip, port=port, password=password, decode_responses=True)
r.set(key, value)
r.get(key)
