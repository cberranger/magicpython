#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import requests,os,bs4,csv
import pymysql
class News(object):
	def __init__(self,title,tags,sendtime):
		self.title = title
		self.tags=tags
		self.sendtime=sendtime

def get_article_title(url):
	articleres=requests.get(url)
	articleres.raise_for_status()
	articlesoup=bs4.BeautifulSoup(articleres.text,'html.parser')
	tags_list=articlesoup.find('meta',{'name':'keywords'}).attrs['content']
	title=articlesoup.h1.get_text()
	createdate=articlesoup.find('div',{'class':'news_bt'}).find('span').text.replace('\r','').replace('\n','').replace('\t','').strip()
	print(createdate)
	news=News(title,tags_list,createdate)
	return news


url=('http://www.jrzj.com/global/')

conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='',charset='utf8')
cur=conn.cursor()
cur.execute('use scraping')

def save(news):
	cur.execute('insert into pages(title,tags,created) values(\"%s\",\"%s\",\"%s\")',(news.title,news.tags,news.sendtime))
	cur.connection.commit()
#i为爬取多少页，每页10条
try:
	for i in range(10):
		print('当前爬取的页面：-------->%s'%url)
		res=requests.get(url)
		res.raise_for_status()
		soup=bs4.BeautifulSoup(res.text,'html.parser')
		#找到div --'zuixinfabu'--->找到所有dd标签
		dd_list=soup.find('div',{'class':'zuixinfabu'}).findAll('dd')
		#遍历所有dd标签，取得每篇文章的链接
		for dd in dd_list:
			articleUrl=dd.find('a',{'target':'_blank'}).get('href')
			print('正在爬取:----->%s'%articleUrl)
			news=get_article_title(articleUrl)
			save(news)
		prevLinks=soup.find('div',{'class':'fy_big'}).findAll('a',{'class':'a1'})
		for prevLink in prevLinks:
			if prevLink.get_text()=='下一页':
				url='http://www.jrzj.com/global/'+prevLink.get('href')
	print('Done')
finally:
	cur.close()
	conn.close()



