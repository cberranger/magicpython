#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import requests,random,os,json,bs4
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
    print(host)
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

def get_music_with_nickname(nickname):
    url='https://music.163.com'
    url_new='https://music.163.com/#/search/m/?s=花添小窗浓&type=1002'
    headers=setHeader(url)
    bsObj=requests.session()
    response=bsObj.get(url_new,headers=headers)
    print(response.status_code)
    soup=bs4.BeautifulSoup(response.text,'html.parser')
	#找到div --'zuixinfabu'--->找到所有dd标签
    dd_list=soup.find('div',{'class':'ttc'})
    print(dd_list)
	

user_agents=load_user_agent()
get_music_with_nickname('花添小窗浓')