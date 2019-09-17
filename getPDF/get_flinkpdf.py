#!/usr/bin/env python3
# -*- coding:utf-8-*-
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import requests
import os
import re


def get_file(file_url, file_name):
    os.makedirs('download', exist_ok=True)
    print('下载了--->'+file_name)
    urlretrieve(file_url, 'download/'+file_name)


url = 'https://github.com/flink-china/flink-training-course'
bsObj = requests.session()
bsObj = BeautifulSoup(bsObj.get(url).content, 'html.parser')
l = bsObj.find(
    'article', {'class': 'markdown-body entry-content p-5'}).findAll("h3")
for ll in l:
    a = ll.find_next_sibling('p').find('a')
    if a != None and a.attrs['href'].endswith('.pdf'):
        name = ll.text.replace('/', '、')
        url = a.attrs['href']
        print(name, ":", url)
        get_file(url, name+'.pdf')
