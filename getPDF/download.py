#!/usr/bin/env python3
#-*- coding:utf-8-*-
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import requests
import os
def get_file(file_url,file_name):
	os.makedirs('download',exist_ok=True)
	print('下载了--->'+file_name)
	urlretrieve(file_url,'download/'+file_name)


url='http://www.sdedu.gov.cn/sdjy/_ztzl/810993/917785/index.html'
bsObj=requests.session()
bsObj=BeautifulSoup(bsObj.get(url).content,'html.parser')
l=bsObj.find('table',align='center').findAll('tr')
for ll in l:
	p=ll.find('p',align='left')
	filelist=ll.findAll('a')
	for f in filelist:
		if f.attrs['href'].startswith('/'):
			a='http://www.sdedu.gov.cn'+f.attrs['href']
			print(a)
			filename=p.get_text()+f.get_text()
			print(filename)
			get_file(a,filename)
