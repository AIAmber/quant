import requests
import re
import os
import base64
import time

dataNum = 'sz000672'
url = "http://120.76.145.62/test/testMult.html"

def reqData(url, dataNum):
	r = requests.get(url)
	rTextBytes = bytes(r.text, encoding = 'utf-8')
	rBase64Text = base64.b64decode(rTextBytes)
	rText = str(rBase64Text, encoding = 'utf-8')
	# r.status_code

	# print(r.text)

	stripSlice = "'var hq_str_"+dataNum+"=\""
	dataSlice = rText.lstrip(stripSlice).split(',')
	# print(dataSlice)

	line0 = "Name: {0[0]},\t Price: {0[3]}.\n".format(dataSlice)
	lineOrg = "Open: {0[1]},\t closeLST: {0[2]}.\n".format(dataSlice)
	line1 = "High: {0[4]},\t Low: {0[5]}.\n".format(dataSlice)
	line2 = """
	Sel5: {0[29]},\t Num5: {0[28]}
	Sel4: {0[27]},\t Num4: {0[26]}
	Sel3: {0[25]},\t Num3: {0[24]}
	Sel2: {0[23]},\t Num2: {0[22]}
	Sel1: {0[21]},\t Num1: {0[20]}
	""".format(dataSlice)

	lineMid = "Prc: {0[3]} \t ----- ----".format(dataSlice)

	line3 = """
	Buy1: {0[11]},\t Num1: {0[10]}
	Buy2: {0[13]},\t Num2: {0[12]}
	Buy3: {0[15]},\t Num3: {0[14]}
	Buy4: {0[17]},\t Num4: {0[16]}
	Buy5: {0[19]},\t Num5: {0[18]}
	""".format(dataSlice)

	print(line0, lineOrg, line1, line2, lineMid, line3)

while True:
	reqData(url, dataNum)
	time.sleep(3.5)