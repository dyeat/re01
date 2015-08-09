import re
import urllib

def gethtml(url):
	html = urllib.urlopen(url)
	scode = html.read()
	return scode

def getImage(source):
	reg = r'src="(*?\.jpg)" ' //抓取圖片副檔名
	imgre = re.compile(reg)
	images = re.findall(imgre,source)
	x = 0
	for i in images:
		urllib.urlretrieve(i,'%s.jpg' % x)
		x+=1 	

source = gethtml('要抓取的網址')
print getImage(source)
