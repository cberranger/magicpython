#!/usr/bin/env python3
#-*-coding : utf-8 -*-
'''
CFDA  数据采集
'''
import requests

class CFDA:

    def __init__(self):
        self.url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'

    def getCfda(self,data):
        self.html=requests.post(self.url,data=data)
        print(self.html)
        dataList=self.html.json()['list']
        for onedata in dataList:
            print(onedata['EPS_NAME'])
            self.write2file(onedata['EPS_NAME'])
        #self.datas=list(map(lambda n:self.html.json()['list'][n]['EPS_NAME'],range(15)))

    def write2file(self,dat):
        with open(r'data.txt','a',encoding='utf-8') as ff:
            ff.write(dat+'\n')

if __name__=='__main__':
    for i in range(1,10):
        cfda=CFDA()
        postData={
            'applyname':'',
            'applysn':'',
            'conditionType':'1',
            'on':'true',
            'page':i,
            'pageSize':100,
            'productName':''
            }

        cfda.getCfda(postData)

