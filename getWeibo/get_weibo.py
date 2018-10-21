#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import requests,random,os,json
from bs4 import BeautifulSoup

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
		'authority':host,
		'Referer': url,
		'User-Agent':user_agent,
		'scheme':'https',
		'cookie':'''''',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	}
	return headers

def get_weibo(url):
	headers=setHeader(url)
	bsObj=requests.session()
	response=bsObj.get(url,headers=headers)
	jsonDict=json.loads(response.text)
	#print(jsonDict)
	userArray=jsonDict['data']['data']
	for i in range(0,len(userArray)-1):
		name=userArray[i]['user']['screen_name']
		with open('name.txt','a') as f:
			f.write(name+"\n")

user_agents=load_user_agent()
#url='https://m.weibo.cn/api/comments/show?id=4296757011387577&page='
url='https://m.weibo.cn/api/statuses/repostTimeline?id=4296757011387577&page='
for i in range(1,100):
    get_weibo(url+str(i))


