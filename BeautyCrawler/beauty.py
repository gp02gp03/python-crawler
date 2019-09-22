import requests
from bs4 import BeautifulSoup #網頁解析工具
from urllib.request import urlopen

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
}

res = requests.get('https://www.ptt.cc/man/Beauty/DF7B/D111/M.1400913738.A.BD8.html',headers=headers)

#print(res.text)

soup = BeautifulSoup(res.text,'html.parser')

images = soup.select('a[href^=http://i.imgur]')

#print(image)

for image in images:
	#print(image['href'])
	filename = image['href'].split('/')[3]
	#print(filename)
	img = urlopen(image['href'])
	with open('./images/' + str(filename),'wb') as f:  #寫入的檔案位置
		f.write(img.read())
