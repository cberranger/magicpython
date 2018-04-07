#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import requests
import re,json
from bs4 import BeautifulSoup
import xlwt
import draw
import time

dataList=[]
for i in range(0,10):
    ksts_time=time.time()
    ksTs='%s_%s' %(int(ksts_time*1000),str(ksts_time)[-3:])
    url=('https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS={}&callback=&q=%E8%BF%90%E5%8A%A8%E8%A3%A4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48').format(i*44,ksTs)
    response=requests.get(url)
    jsonDict=json.loads(response.text)
    itemList=jsonDict['mods']['itemlist']['data']['auctions']
    for item in itemList:
        #print(item['title']+':'+item['price'])
        temp={
            'title':item['raw_title'],
            'price':item['view_price'],
            'location':item['item_loc'],
            'sales':item['view_sales'],
            'nick':item['nick'],
            'detail_url':item['detail_url']
        }
        dataList.append(temp)
#print(dataList)
f=xlwt.Workbook(encoding='utf-8')
sheet01=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
sheet01.write(0,0,'商品名')
sheet01.write(0,1,'价格')
sheet01.write(0,2,'地区')
sheet01.write(0,3,'购买人数')
sheet01.write(0,4,'店铺名称')
sheet01.write(0,5,'购买链接')
for m in range(len(dataList)):
    sheet01.write(m+1,0,dataList[m]['title'])
    sheet01.write(m+1,1,dataList[m]['price'])
    sheet01.write(m+1,2,dataList[m]['location'])
    sheet01.write(m+1,3,dataList[m]['sales'])
    sheet01.write(m+1,4,dataList[m]['nick'])
    sheet01.write(m+1,5,dataList[m]['detail_url'])        


f.save('运动裤.xls')

dataLoc={}
for item_one in dataList:
    dataLoc[item_one['location'].split(' ')[0]]=dataLoc.get(item_one['location'].split(' ')[0],0)+1

draw.pie(dataLoc)






