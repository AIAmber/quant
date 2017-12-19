import requests
import re
import os
import time

dataNum = 'sz000672'
url = "http://hq.sinajs.cn/list="+dataNum
htmlPwd = "/axebox/code/quant/www/test.html"
ins = 0

def reqData(url, dataNum):
	r = requests.get(url)
	# r.status_code

	# print(r.text)

	with open(htmlPwd, 'w') as htmlFile:
		htmlFile.write(r.text)

while ins<4788:
	reqData(url, dataNum)
	time.sleep(1.7)
	ins += 1

# ins = 0
exit()