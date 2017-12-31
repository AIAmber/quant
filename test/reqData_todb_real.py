import requests
import re
import os
import time
import psycopg2

dataNum = 'sz000672'
url = "http://hq.sinajs.cn/list="+dataNum

tableName = 't_stock_sz000672_bak'

databaseName = 'quant'
username = 'postgres'
password = 'Bang103.'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(database = databaseName, user = username, password = password, host = host, port = port)
cur = conn.cursor()

dsls = []
def reqData(url, dataNum):
	r = requests.get(url)
	# r.status_code

	# print(r.text)

	stripSlice = "'var hq_str_"+dataNum+"=\""
	dataSlice = r.text.lstrip(stripSlice).split(',')
	# print(dataSlice)
	# dsls = []
	for dsl in dataSlice:
		dsls.append(dsl)
	# print(dsls)

# dt = reqData(url, dataNum)
	print(dsls)

	cur.execute("INSERT INTO t_stock_sz000672_bak (stock_name, price, open, close_lst, high, low, sel_5, sel_5_num, sel_4, sel_4_num, sel_3, sel_3_num, sel_2, sel_2_num, sel_1, sel_1_num, buy_1, buy_1_num, buy_2, buy_2_num, buy_3, buy_3_num, buy_4, buy_4_num, buy_5, buy_5_num) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (dsls[0], dsls[3], dsls[1], dsls[2], dsls[4], dsls[5], dsls[29], dsls[28], dsls[27], dsls[26], dsls[25], dsls[24], dsls[23], dsls[22], dsls[21], dsls[20], dsls[11], dsls[10], dsls[13], dsls[12], dsls[15], dsls[14], dsls[17], dsls[16], dsls[19], dsls[20]))

	conn.commit()
	# conn.close()
	# print("Success!")

while True:
	reqData(url, dataNum)
	dsls=[]
	time.sleep(3.5)
