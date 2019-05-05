#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import requests,random,os,json
from bs4 import BeautifulSoup
import xlwt


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

def get_jobinfo(url):
	dataList=[]
	headers=setHeader(url)
	bsObj=requests.session()
	response=bsObj.get(url,headers=headers)
	jsonDict=json.loads(response.text)
	#print(jsonDict)
	userArray=jsonDict['data']['results']
	#print(userArray)
	for i in range(0,len(userArray)-1):
		temp={
			'companyName':userArray[i]['company']['name'],
			'area':'未知' if  (('businessArea') not in userArray[i] ) else userArray[i]['businessArea'],
			'jobName':userArray[i]['jobName'],
			'salary':userArray[i]['salary'],
			'updateDate':userArray[i]['updateDate'],
			'companyType':userArray[i]['company']['type']['name'],
			'positionURL':userArray[i]['positionURL']
		}
		print(temp)
		dataList.append(temp)
	f=xlwt.Workbook(encoding='utf-8')
	sheet01=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
	sheet01.write(0,0,'公司名')
	sheet01.write(0,1,'地区')
	sheet01.write(0,2,'职位名称')
	sheet01.write(0,3,'薪资')
	sheet01.write(0,4,'更新日期')
	sheet01.write(0,5,'企业类型')
	sheet01.write(0,5,'职位链接')
	for m in range(len(dataList)):
		sheet01.write(m+1,0,dataList[m]['companyName'])
		sheet01.write(m+1,1,dataList[m]['area'])
		sheet01.write(m+1,2,dataList[m]['jobName'])
		sheet01.write(m+1,3,dataList[m]['salary'])
		sheet01.write(m+1,4,dataList[m]['updateDate'])
		sheet01.write(m+1,5,dataList[m]['companyType'])  
		sheet01.write(m+1,6,dataList[m]['positionURL'])  
	f.save('招聘信息.xls')

	

user_agents=load_user_agent()
for i in range(0,1):
	url='https://fe-api.zhaopin.com/c/i/sou?start='+str(i*90)+'&pageSize=90&cityId=702&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.31803229&x-zp-page-request-id=b64b9303e5d34db5a4a528770e68d4ef-1557055947992-764249'
	print(url)
	try:
		get_jobinfo(url)
	except KeyError as identifier:
		i=i-1
		pass
	continue
	
