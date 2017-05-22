#!/usr/bin/env python3
#-*-coding:utf-8
from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve

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
data="""
__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKMTY1NjcyNzU1Ng9kFgJmD2QWBgIBD2QWBgIDDxYCHgpvbmtleXByZXNzBRhFbnRlclRleHRCb3goJ2J0blNlYXJoJylkAgUPFgIfAAUZRW50ZXJUZXh0Qm94MSgnYnRuTG9naW4nKWQCBg8WAh8ABRlFbnRlclRleHRCb3gxKCdidG5Mb2dpbicpZAIDDxYCHwAFIEVudGVyVGV4dEJveFMoJ2J0blNlYXJoQ29tbW5ldCcpZAIFDxAPFgYeDURhdGFUZXh0RmllbGQFB2NvbnRlbnQeDkRhdGFWYWx1ZUZpZWxkBQdkZXB0X2lkHgtfIURhdGFCb3VuZGdkEBUpCeWKnuWFrOWupDzljJfkuqzljY7nlLXljZPor4bkv6Hmga%2FlronlhajmtYvor4TmioDmnK%2FkuK3lv4PmnInpmZDlhazlj7gS5YyX5Lqs6JCl6ZSA5Lit5b%2BDCei0ouWKoemDqBjljoLnq5noh6rliqjljJbkuovkuJrpg6gP5Yib5paw56CU56m26ZmiIeeUtemHj%2BS4juiQpemUgOS%2FoeaBr%2BWMluS6i%2BS4mumDqBXnlLXnvZHpg6jku7%2FnnJ%2FkuK3lv4MY55S1572R6Ieq5Yqo5YyW5LqL5Lia6YOoCeiRo%2BS6i%2BS8mhLokaPkuovkvJrlip7lhazlrqQJ5L6b5bqU6YOoGOenr%2BaIkOiDvea6kOaciemZkOWFrOWPuBjnp6%2FmiJDova%2Fku7bmnInpmZDlhazlj7gJ5Z%2B65bu66YOoD%2BmbhuWboueuoeeQhumDqAnnm5HkuovkvJoY5Lqk6YCa5paw6IO95rqQ5LqL5Lia6YOoGOmFjee9keiHquWKqOWMluS6i%2BS4mumDqA%2FkvIHkuJrlj5HlsZXpg6gY5LyB5Lia6IO95rqQ566h55CG5Lit5b%2BDHumdkuWym%2Benr%2BaIkOeUteWtkOaciemZkOWFrOWPuBXkurrlipvooYzmlL%2FnrqHnkIbpg6gk5bGx5Lic5a6J5o6n5L%2Bh5oGv56eR5oqA5pyJ6ZmQ5YWs5Y%2B4J%2BWxseS4nOenr%2BaIkOS4reeJqeaWsOadkOaWmeaciemZkOWFrOWPuBLmt7HlnLPorr7orqHkuK3lv4MP5biC5Zy65Y%2BR5bGV6YOoD%2BeglOWPkeeuoeeQhumDqAznoJTlj5HkuK3lv4MS6JCl6ZSA5YyX5pa55aSn5Yy6EuiQpemUgOa1t%2BWkluWkp%2BWMuhLokKXplIDljY7kuJzlpKfljLoS6JCl6ZSA5Y2O5Lit5aSn5Yy6EuiQpemUgOWNl%2BaWueWkp%2BWMuhLokKXplIDopb%2FljJflpKfljLoS6JCl6ZSA6KW%2F5Y2X5aSn5Yy6EuiQpemUgOebtOWxnuecgeWMug%2Fov5DokKXnrqHnkIbpg6gM5Yi26YCg5Lit5b%2BDEui0qOmHj%2BeuoeeQhuS4reW%2FgxLmgLvnu4%2FnkIblip7lhazkvJoVKQE4AjU5AjYwAjE0AjIyAjYxAjI1AjU4AjI0ATIBNgI0NgI2MgI2NQI1NAI2OQEzAjc0AjQ0AjczAjQwAjI3AjcyAjY4AjY3AjU1AjE1AjUzAjIxAjI5AjY0AjM3AjMxAjMwAjU2AjY2AjU3AjQzAjEyAjM2ATQUKwMpZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cWAWZkZGubgcIhcKnaGmOb5SXTgCv9T3EGtcRG0zUmZQ0w%2BfLF&__EVENTVALIDATION=%2FwEdAEPNu3dU5JO4pvobTdUUah%2FupK8gocPqfZUCCpzh2r%2BjmA7q62%2BXhUXFg0QMfa%2BWM5qyLBKdSRtpirmAb%2FnxD6eVDy1%2Bil%2BkLVNjOvBpbmssygmW2bSLTm1VbzUYV6H%2BCJMYdYK3wClhf%2B1hIqUWBaeOS9CXEQVwKbugNosHWaE05ROEdcA19Qet7U08zXlOc7ktYAzBGTdKyXWGmbS9HlKF3vuS%2F15wkstbLIbxG%2BGBBj9RlQpOaPBFAn1vdil2dNy2dqu%2BSaeSXEydHOyi3AWDPvkkQa8iJ0%2BJsMMinwSxWJ5VlPFTNw9wLHCGA7GG0bnjOThw7JP%2BQ%2FtC1X84U1tLXv9kcx%2BoVcsoJtsh8PP%2BlXW2F03ojkequNuaOqWuGLWZ3janCF%2F9ngplYIET01y9ZDWZtGkFEDS6GPLY7RUeY%2BTvGqrIIlErSBYBJSlSAhelfJi7nksHBdWLJcRCSygrPgZIxqifykUYaM8GabaBxXDv6BPK3yFI3LjO9yW0EoD9ZQ7EKdLeJ%2B9KtgsvKxSAU%2BNmMmxjbMOfRFIHw31nu8SN%2BpDhXAu3nG6zjBV0AA%2FjOXHeJAXJrfEiXTUMX9z1k3lQTkfYYkq7EH7eSUe6O%2FAtmJHVJGE%2FLB7oKUKb9BGC1sLGsbaZlrmVax775lvekPgpZOBGbjdWD3Fpbk79qzXyPEXZowwco%2F6l1MqYjZN2dDuSmla8U8xKMvcVSHSSBLPqd0Ugud5m7plm9c2%2BQcau%2F5R5QgmgA73ixJAQWV5JuKDGWXoCXdFCwQ8kY3sLRZIuEIOgcu%2FYcjF6Sr%2BY6GQMOh%2FzjPS2EW8ppd9x4k%2F01bgmi4fr4aCHgJo50Ro%2BtmeAa1x16oyU%2BdFjJduegx%2Bij4EX26ePHLjO92BpX4YZFefMmipDIQGx6eJ00I%2Bp5dqht0qlqnk%2FwBkFhdcQ6ZMJ7oif8kRvrUsvRHkY2%2B%2FsHtHCFHCSHJzESc5D0q2xAHleLJvTIhjKS5DDYXJSIyH60PDgyCWFi8pxCI4h1iWW6q3%2BwnC%2BjWVLm%2F8JVByPZ6Qo9QrkmyVVoWWChXgJi%2FLDSuKbyqSF6W30ldN3tYeX2pjRZsQITGch8Mg%2FFaFm7Mw1hHWCBqpyahtkgLpnXBgh4LkKKzLsEaHyblNVnQR5011rW6ZegezchOE%2FdZtKF%2BoSlU71JX0%2F7MTi3VXezOUBH4oiXHwZlQWCbOWQwh8M%2BXIo%2Fk5ylb1jeatFxvwUp4M4qBDIIzyaV8sOSnhwSsDQBHEIBemsPjInUkpL40GVjO7PPzd4kAnJvt%2FT%2B3RkbTy3vDXXLIayvUrLgkXD2OhHtBQqQGZu6G7P%2BIsjy3GUpYx%2BWnHLAxsyurWz5r%2FBaDbMZPH5fFhtkk8wy4LB7yUxPD0WenoS7QPSDfCuSOsyEPHFeMPhzGVPcd1TPw8CGSJPV3KcQlu6%2F6t%2BZ1EwKx9knDvcN2u54SpRAgCON7k%3D&top1%24SearchTypeMenu=%E6%8C%89%E6%A0%8F%E7%9B%AE&top1%24SearchTypeTime=%E6%8C%89%E6%97%B6%E9%97%B4&top1%24SearchKey=&top1%24Oper_Pwd=&top1%24Oper_Name=%E8%BE%93%E5%85%A5%E5%B8%90%E5%8F%B7&T1=%25&D1=8&btnSearhCommnet=%E6%90%9C%E7%B4%A2
"""


def getContact():
	url="http://share.ieslab.cn/addressbook.aspx"
	html=requests.get(url).content
	bsObj=BeautifulSoup(html,'html.parser')
	#print(bsObj.content)
	VIEWSTATE=bsObj.find('input',{'id':'__VIEWSTATE'}).attrs['value']
	EVENTVALIDATION=bsObj.find('input',{'id':'__EVENTVALIDATION'}).attrs['value']
	#print(VIEWSTATE)
	#print(EVENTVALIDATION)
	payload={
				'__EVENTTARGET':'',
				'__EVENTARGUMENT':'',
				'__LASTFOCUS':'',
				'__VIEWSTATE':VIEWSTATE,
				'__EVENTVALIDATION':EVENTVALIDATION,
				'T1':'%',
				'D1':8,
				'btnSearhCommnet':'搜索'
				}
	contacthtml=requests.post(url,data=payload).content
	contactObj=BeautifulSoup(contacthtml,'html.parser')
	table=contactObj.find('table',{'class':'recipe'})
	html=html_template.format(content=table)
	html = html.encode("utf-8")
	#print(table)
	with open('contact.html','wb') as f:
		f.write(html)

getContact()
