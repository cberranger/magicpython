#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import requests
import re,json
from bs4 import BeautifulSoup
import xlwt
def parseJsonp(jsonpStr):
    try:
        return re.search('^[^(]*?\((.*)\)[^)]*$', jsonpStr).group(1)
    except:
        raise ValueError('Invalid JSONP')

def write2file(dat):
    with open(r'data.txt','a',encoding='utf-8') as ff:
        ff.write(dat+'\n')


    
    

'''
url='https://s.taobao.com/search?data-key=s&data-value=144&ajax=true&_ksTS=1522975688691_652&callback=&q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&p4ppushleft=5%2C48'
response=requests.get(url)
jsonDict=json.loads(response.text)
itemList=jsonDict['mods']['grid']['data']['spus']
for item in itemList:
    print(item['title']+':'+item['price'])
'''

dataList=[]
for i in range(0,10):
    url=('https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS=1522975688691_652&callback=&q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&p4ppushleft=5%2C48').format(i*48)
    response=requests.get(url)
    jsonDict=json.loads(response.text)
    itemList=jsonDict['mods']['grid']['data']['spus']
    for item in itemList:
        #print(item['title']+':'+item['price'])
        temp={
            'title':item['title'],
            'price':item['price']
        }
        dataList.append(temp)
print(dataList)
f=xlwt.Workbook(encoding='utf-8')
sheet01=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
sheet01.write(0,0,'商品名')
sheet01.write(0,1,'价格')
for m in range(len(dataList)):
    sheet01.write(m+1,0,dataList[m]['title'])
    sheet01.write(m+1,1,dataList[m]['price'])

f.save('手机.xls')





