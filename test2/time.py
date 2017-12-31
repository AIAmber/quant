import time
import os

todTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
todTimeStamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

print(todTime, todTimeStamp)

with open('./create_msq_text.sql') as f:
	sqlText = f.read()
	print(sqlText)

todTimeSim = time.strftime('%Y%m%d', time.localtime(time.time()))
# print(todTimeSim)
tableName = 't_stock_sz000672_' + todTimeSim[2:]
print(tableName)