import requests
import re
import os

dataNum = 'sz000672'
url = "http://hq.sinajs.cn/list="+dataNum

r = requests.get(url)
# r.status_code

# print(r.text)

stripSlice = "'var hq_str_"+dataNum+"=\""
dataSlice = r.text.lstrip(stripSlice).split(',')
# print(dataSlice)
dsls = []
for dsl in dataSlice:
	dsls.append(dsl)
# print(dsls)

# dt = reqData(url, dataNum)
print(dsls)

print(dsls[8], dsls[9])
volume = dsls[8]
turnVolume = dsls[9]
timeStamp = dsls[30] + ' ' +  dsls[31]

print(volume, turnVolume, timeStamp)
