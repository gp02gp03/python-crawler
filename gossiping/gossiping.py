import requests
from bs4 import BeautifulSoup #網頁解析工具
from urllib.request import urlopen

payload = {
	'from': '/bbs/Gossiping/index.html',
	'yes':'yes'
}

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
}

rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18',data=payload,headers=headers) 
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html',headers=headers)
#print(res.text)

soup = BeautifulSoup(res.text,'html.parser')
items = soup.select('.r-ent')

#print(items)

for item in items:
	#print('日期',format(item.select('.data')[0].text))
	print(item.select('.date')[0].text,item.select('.author')[0].text,item.select('.title')[0].text)
