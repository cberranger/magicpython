#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import requests
import os
import bs4
import base64
from urllib.request import urlretrieve

# 下载图片
'''
将图片保存到本地
'''


def get_image(image_url, image_name):
    os.makedirs('images', exist_ok=True)
    print('下载了--->'+image_name)
    urlretrieve(image_url, 'images/'+image_name)


def write_file(str_title, str_content):
    os.makedirs('base64', exist_ok=True)
    with open('base64/'+str_title+'.txt', 'a') as f:
        f.write(str_content)


url = 'https://www.xinli001.com/ceshi/1631/start'
print('Dowloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
dd_list = soup.findAll('div', {'class': 'test_contents'})
print(dd_list)
i = 1
for d in dd_list:
    name = d.find('p', {'class': 'descs fb'}).get_text()
    image_url = d.find('img').get('src')
    print(name, ":", image_url)
    get_image(image_url, str(i)+".png")
    i = i+1
print('Done')

for a in range(1, 61):
    with open("images/"+str(a)+'.png', 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        write_file(str(a), s)
print(' base64 Done')
