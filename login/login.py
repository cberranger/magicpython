#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os,random
#from myutils import load_user_agent
# 首先发起一次请求来获取参数名和验证码等



#加载user_agents配置文件
def load_user_agent():
	user_agents=[]
	fp = open('user_agents', 'r')
	line  = fp.readline().strip('\n')
	while(line):
		user_agents.append(line)
		line = fp.readline().strip('\n')
	fp.close()
	return user_agents


#设置请求头
def setHeader(url):
	#抽取URL中的主机名
	host=url.replace('https://','')
	length = len(user_agents)
	index=random.randint(0,length-1)
	user_agent = user_agents[index]
	headers={
		'Referer': url,
		'Host':host,
		'User-Agent':user_agent,
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	}
	return headers

def getParams(url):
	headers=setHeader(url)
	bsObj=requests.session()
	paramDoc=bsObj.get(url,headers=headers)
	print(paramDoc.status_code)
	bsObj=BeautifulSoup(paramDoc.content,'html.parser')
	for inmark in bsObj.find_all('input'):
		name=inmark.attrs['name']
		print(name)



user_agents=load_user_agent()
url='https://www.v2ex.com/signin'
getParams(url)
