import re,requests,random,os,json,time


user_agents=[]
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
		'cookie':'''PB3_SESSION="2|1:0|10:1511533780|11:PB3_SESSION|40:djJleDoxNzEuMjEwLjIxMy42Njo5MTIwOTM0OQ==|e009e48c1123d62634b84b4042b1738071babb5b958a2bfad37e1cd3df6aaf90"; V2EX_TAB="2|1:0|10:1511535264|8:V2EX_TAB|8:dGVjaA==|dc85fae96ecd358395251f7b8dd4b262b8c7539186567c07d64bbd5c506dbaa1"; _gat=1; V2EX_LANG=zhcn; _ga=GA1.2.768685691.1494208860; _gid=GA1.2.522141493.1511533782''',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	}
	return headers



def get_one_page(url):
    response = requests.get(url,headers=setHeader(url))
    print(response.status_code)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    expression='<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.8?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
    pattern=re.compile(expression,re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3])>3 else '' ,
            'time':item[4].strip()[5:] if len(item[4])>5 else '',
            'score':item[5].strip()+item[6].strip()
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
    


user_agents=load_user_agent()   
url = 'http://maoyan.com/board/4'
html = get_one_page(url)
for item in parse_one_page(html):
    print(item)
    write_to_file(item)
