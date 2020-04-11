#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import requests,os,bs4,csv

def get_article_title(url):
	articleres=requests.get(url)
	articleres.raise_for_status()
	articlesoup=bs4.BeautifulSoup(articleres.text,'html.parser')
	tags_list=articlesoup.find('meta',{'name':'keywords'}).attrs['content']
	title=articlesoup.h1.get_text()
	createdate=articlesoup.find('div',{'class':'news_bt'}).find('span').text
	with open('articels.csv','a') as f:
		writer=csv.writer(f)
		writer.writerow((title,tags_list,createdate))

url=('http://www.jrzj.com/global/')
with open('articels.csv','w') as f:
	writer=csv.writer(f)
	writer.writerow(('title','tag','posttime'))
#while url!='http://www.jrzj.com/global/list-9-1483-0.html':

# i is how many pages to crawl, 10 is how many per page
for i in range(10):
	print('Currently Crawled Pages：-------->%s'%url)
	res=requests.get(url)
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,'html.parser')
	# Find div-'zuixinfabu' ---> find all dd tags
	dd_list=soup.find('div',{'class':'zuixinfabu'}).findAll('dd')
	# Traverse all dd tags to get a link to each article	for dd in dd_list:
		articleUrl=dd.find('a',{'target':'_blank'}).get('href')
		print('Crawling:----->%s'%articleUrl)
		get_article_title(articleUrl)

	prevLinks=soup.find('div',{'class':'fy_big'}).findAll('a',{'class':'a1'})
	for prevLink in prevLinks:
		if prevLink.get_text()=='下一页':
			url='http://www.jrzj.com/global/'+prevLink.get('href')

print('Done')


	
