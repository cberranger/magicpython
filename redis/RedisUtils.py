#!/usr/bin/env python3
# -*-coding : utf-8 -*-
# author magicdu

import os
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import redis


# 加载yaml文件
def loadYmlConfig():
    file = open('config.yml', 'r', encoding='utf-8')
    stream = file.read()
    config = yaml.load(stream, Loader=Loader)
    return config


# 获取 yaml 文件的 某个节点的 配置
def getConfig(key):
    keyConfig = loadYmlConfig()[key]
    print(keyConfig)
    return keyConfig


# 获取redis配置
def getRedisConfig():
    ymlconfig = getConfig('redis')
    redisConfig = RedisConfig(
        ymlconfig['host'], ymlconfig['port'], ymlconfig['password'], ymlconfig['decode_responses'], ymlconfig['max_connections'])
    return redisConfig


# 获取 redis 连接
def getRedisConnection():
    config = getRedisConfig()
    connection = redis.Redis(host=config.host, port=config.port,
                             password=config.password, decode_responses=config.decode_responses)
    return connection

# 获取 redis 连接池


def getRedisConnectionPool():
    config = getRedisConfig()
    pool = redis.ConnectionPool(host=config.host, port=config.port,
                                password=config.password, max_connections=config.max_connections)
    return pool


# 使用连接池获取 redis 连接
def getRedisConnectionWithPool():
    pool = getRedisConnectionPool()
    connection = redis.Redis(connection_pool=pool)
    return connection


# redis 配置
class RedisConfig(object):
    def __init__(self, host, port, password, decode_responses, max_connections):
        self.host = host
        self.port = port
        self.password = password
        self.decode_responses = decode_responses
        self.max_connections = max_connections
