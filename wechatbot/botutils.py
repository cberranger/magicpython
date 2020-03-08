#!/usr/bin/env python3
# -*-coding : utf-8 -*-
# author magicdu

import os
import time
import requests
import json
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# 加载yaml文件
def loadYmlConfig():
    file = open('bootstrap.yml', 'r', encoding='utf-8')
    stream = file.read()
    config = yaml.load(stream, Loader=Loader)
    return config


# 获取 yaml 文件的 某个节点的 配置
def getConfig(key):
    keyConfig = loadYmlConfig()[key]
    print(keyConfig)
    return keyConfig

# 获取企业号的配置
def getBotConfig():
    ymlconfig = getConfig('wechatbot')
    botConfig = WechatBotConfig(
        ymlconfig['appid'], ymlconfig['agentid'], ymlconfig['secret'], ymlconfig['bot_access_token_url'], ymlconfig['send_msg_url'])
    return botConfig

# 获取 token 
def get_access_token(config):
        values = {'corpid': config.appid,
                  'corpsecret': config.secret,
                  }
        req = requests.post(config.bot_access_token_url, params=values)
        data = json.loads(req.text)
        return data["access_token"]

# 获取 access_token 并缓存到本地 
# token 过期时重新获取
def get_bot_access_token(config):
        try:
            with open('./tmp/access_token.conf', 'r') as f:
                t, access_token = f.read().split()
        except:
            with open('./tmp/access_token.conf', 'w') as f:
                access_token = get_access_token(config)
                cur_time = time.time()
                f.write('\t'.join([str(cur_time), access_token]))
                return access_token
        else:
            cur_time = time.time()
            if 0 < cur_time - float(t) < 7260:
                return access_token
            else:
                with open('./tmp/access_token.conf', 'w') as f:
                    access_token = get_access_token(config)
                    f.write('\t'.join([str(cur_time), access_token]))
                    return access_token

## 发送消息
def send_data(config,userids,message):
        send_url = config.send_msg_url + get_bot_access_token(config)
        send_values = {
            "touser": userids,
            "msgtype": "text",
            "agentid": config.agentid,
            "text": {
                "content": message
                },
            "safe": "0"
            }
        send_msges=(bytes(json.dumps(send_values), 'utf-8'))
        respone = requests.post(send_url, send_msges)
        respone = respone.json()   #当返回的数据是json串的时候直接用.json即可将respone转换成字典
        print(respone)
        return respone["errmsg"]

# 企业号 配置
class WechatBotConfig(object):
    def __init__(self, appid, agentid, secret, bot_access_token_url, send_msg_url):
        self.appid = appid
        self.agentid = agentid
        self.secret = secret
        self.bot_access_token_url = bot_access_token_url
        self.send_msg_url=send_msg_url
