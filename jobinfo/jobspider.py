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

# 将信息写入excel
def writelist2excel(head_list_alias,head_list,data_list,file_name):
	f=xlwt.Workbook(encoding='utf-8')
	sheet01=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
	for i in range(len(head_list_alias)):
		sheet01.write(0,i,head_list_alias[i])
	for m in range(len(data_list)):
		for n in range(len(head_list)):
			sheet01.write(m+1,n,data_list[m][head_list[n]])
	f.save(file_name+'.xls')

# 获取职位信息
def get_jobinfo(url):
	dataList=[]
	headers=setHeader(url)
	bsObj=requests.session()
	response=bsObj.get(url,headers=headers)
	jsonDict=json.loads(response.text)
	userArray=jsonDict['data']['results']
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
		dataList.append(temp)
	return dataList

	

user_agents=load_user_agent()
data_l=[]
head_l_a=['公司名','工作地点','职位名称','薪资','更新日期','公司类型','职位链接']
head_l=['companyName','area','jobName','salary','updateDate','companyType','positionURL']
for i in range(0,12):
	url='https://fe-api.zhaopin.com/c/i/sou?start='+str(i*90)+'&pageSize=90&cityId=702&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.31803229&x-zp-page-request-id=b64b9303e5d34db5a4a528770e68d4ef-1557055947992-764249'
	try:
		data_l+=get_jobinfo(url)
	except KeyError as identifier:
		i=i-1
		pass
	continue
print(len(data_l))
writelist2excel(head_l_a,head_l,data_l,'招聘信息')	
