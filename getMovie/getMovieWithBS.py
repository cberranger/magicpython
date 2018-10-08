#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os,random,csv


#新闻类
class Movie(object):
	def __init__(self,title,star,time):
		self.title = title     #标题
		self.star=star         #明星
		self.time=time #上映时间

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
		'cookie':'''PB3_SESSION="2|1:0|10:1511533780|11:PB3_SESSION|40:djJleDoxNzEuMjEwLjIxMy42Njo5MTIwOTM0OQ==|e009e48c1123d62634b84b4042b1738071babb5b958a2bfad37e1cd3df6aaf90"; V2EX_TAB="2|1:0|10:1511535264|8:V2EX_TAB|8:dGVjaA==|dc85fae96ecd358395251f7b8dd4b262b8c7539186567c07d64bbd5c506dbaa1"; _gat=1; V2EX_LANG=zhcn; _ga=GA1.2.768685691.1494208860; _gid=GA1.2.522141493.1511533782''',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	}
	return headers

def getMovie(url):
    headers=setHeader(url)
    bsObj=requests.session()
    paramDoc=bsObj.get(url,headers=headers)
    print(paramDoc.status_code)
    bsObj=BeautifulSoup(paramDoc.content,'html.parser')
    for inmark in bsObj.find_all('div',{'class':'movie-item-info'}):
        title=inmark.find('p',{'class':'name'}).get_text()
        star=inmark.find('p',{'class':'star'}).get_text()
        time=inmark.find('p',{'class':'releasetime'}).get_text()
        print('影片名称:'+title+star+time+"\n\t")
        with open('movie.csv','a') as f:
            writer=csv.writer(f)
            writer.writerow((title,star,time))



user_agents=load_user_agent()
url='http://maoyan.com/board/4?offset='
for i in range(0,10):
    getMovie(url+str(i))
