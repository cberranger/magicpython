#!/usr/bin/env python3
#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import pdfkit
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }

'''
url:the html page you want to convert to pdf
tag:html tag   ex:'div'
name: attr name   ex:'class'
value: attr value  ex:'article'
'''
def html2pdf(url,tag,name,value):
	html=requests.get(url).content
	bsObj=BeautifulSoup(html,'html.parser')
	title=bsObj.h1
	content=bsObj.find(tag,{name:value})
	content.insert(1,title)
	filename=content.h1.get_text()
	html=html_template.format(content=content)
	html = html.encode("utf-8")
	with open(filename+'.html', 'wb') as f:
		f.write(html)
	pdfkit.from_file(filename+'.html',filename+'.pdf',options=options)

'''
example
'''
url='http://www.51testing.com/html/71/410671-845364.html'
html2pdf(url,'div','class','xspace-layout1')
