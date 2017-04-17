#!/usr/bin/env python3
#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import os,random
import re
user_agents=list()
#加载 user_agents配置文件
def load_user_agent():
	fp = open('user_agents', 'r')
	line  = fp.readline().strip('\n')
	while(line):
		user_agents.append(line)
		line = fp.readline().strip('\n')
	fp.close()

def write_file(str_title,content):
	with open(str_title+'.txt','w') as f:
		f.write(content)

def get_news(link):
	length = len(user_agents)
	index=random.randint(0,length-1)
	user_agent = user_agents[index]
	headers={
		'Referer': 'http://news.sohu.com',
		'Host':'news.sohu.com',
		'User-Agent':user_agent,
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	}
	bsObj=requests.session()
	bsObj=BeautifulSoup(bsObj.get(link,headers=headers).content,'html.parser')
	title=bsObj.h1.get_text()
	content=bsObj.find('div',{'itemprop':'articleBody'})
	script=content.findAll('script')
	for sc in script:
		sc.extract()
	content=content.get_text()
	write_file(title,content)


load_user_agent()
url='http://news.sohu.com'
length = len(user_agents)
index=random.randint(0,length-1)
user_agent = user_agents[index]
headers={
	'Referer': 'http://news.sohu.com',
	'Host':'news.sohu.com',
	'User-Agent':user_agent,
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
html=requests.session()
html=html.get(url,headers=headers).content
html=html.decode('gb2312','ignore').encode('utf-8')
bsobj=BeautifulSoup(html,'html.parser')
r=bsobj.find('div',{'class':'r'})
alist=r.findAll('a')
for link in alist:
	href=link.attrs['href']
	if re.match('^(http://news.sohu.com/)[0-9]{8}\/n[0-9]{9}(.shtml)$',href):
		get_news(href)