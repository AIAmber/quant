import requests
import re
import os
import time

dataNum = 'sz000672'
url = "http://hq.sinajs.cn/list="+dataNum
htmlPwd = "/axebox/code/quant/www/test.html"

def reqData(url, dataNum):
	r = requests.get(url)
	# r.status_code

	print(r.text)

	with open(htmlPwd) as htmlFile:
		htmlFile.write(r.text)

while True:
	reqData(url, dataNum)
	time.sleep(1.7)