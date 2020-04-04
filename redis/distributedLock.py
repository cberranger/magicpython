#!/usr/bin/env python3
# -*-coding : utf-8 -*-
import redis

LOCK_EXPIRE = 100

# 锁对象
class Lock(object):
     def __init__(self, name, value):
        self.name = name
        self.value = value

#获得锁
def getLock(conn, lock, lockExpireTime):
    if lock.name == '' or lock.value == '':
        return False
    if conn.setnx(lock.name, lock.value):
        conn.expire(lock.name,lockExpireTime)
        return True
    else:
        return False

# 尝试获得锁
def tryLock(conn, lock):
    return getLock(conn,lock,LOCK_EXPIRE)       
    
# 释放锁
def releaseLock(conn, lock):
    if lock.name != '':
        conn.delete(lock.name)
        