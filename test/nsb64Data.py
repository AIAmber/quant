import requests
import re
import os
import base64
import time

dataNum = 'sz000672'
url = "http://hq.sinajs.cn/list="+dataNum
htmlPwd = "/axebox/code/quant/www/ntestMult.html"
ins = 0

def reqData(url, dataNum):
	r = requests.get(url)
	rTextBytes = bytes(r.text, encoding='utf-8')
	rTextBase64 = base64.b64encode(rTextBytes)
	rTextBase64Str = str(rTextBase64, encoding='utf-8')
	# r.status_code

	# print(r.text)

	with open(htmlPwd, 'w') as htmlFile:
		htmlFile.write(rTextBase64Str)

while True:
	reqData(url, dataNum)
	time.sleep(1.7)
	ins += 1

# ins = 0
exit()