import requests
import re
import os
import time
import MySQLdb

dataNum = 'sz000672'
url = "http://hq.sinajs.cn/list="+dataNum

tableName = 't_stock_sz000672_bak'

databaseName = 'quant'
username = 'root'
password = 'Bang103.'
host = '120.76.145.62'
port = 3306

conn = MySQLdb.connect(host=host, port=port, user=username, passwd=password, db=databaseName)
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

	cur.execute("INSERT INTO t_stock_sz000672_bak (price, open_tod, close_lst, high, low, sel_5, sel_5_num, sel_4, sel_4_num, sel_3, sel_3_num, sel_2, sel_2_num, sel_1, sel_1_num, buy_1, buy_1_num, buy_2, buy_2_num, buy_3, buy_3_num, buy_4, buy_4_num, buy_5, buy_5_num) VALUES (%f, %f, %f, %f, %f, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d)" %(float(dsls[3]), float(dsls[1]), float(dsls[2]), float(dsls[4]), float(dsls[5]), float(dsls[29]), int(dsls[28]), float(dsls[27]), int(dsls[26]), float(dsls[25]), int(dsls[24]), float(dsls[23]), int(dsls[22]), float(dsls[21]), int(dsls[20]), float(dsls[11]), int(dsls[10]), float(dsls[13]), int(dsls[12]), float(dsls[15]), int(dsls[14]), float(dsls[17]), int(dsls[16]), float(dsls[19]), int(dsls[18])))
	# cur.execute("INSERT INTO t_stock_sz000672_bak (stock_name, price, sel_5, sel_5_num) VALUES (%s, %f, %f, %d)" (dsls[0], float(dsls[3]),  float(dsls[29]), int(dsls[28])))
	# cur.execute("INSERT INTO t_stock_sz000672_bak (price, open_tod, close_lst, high, low, sel_5, sel_5_num, sel_4, sel_4_num, sel_3, sel_3_num) VALUES (%f, %f, %f, %f, %f, %f, %d, %f, %d, %f, %d)" %(float(dsls[3]), float(dsls[1]), float(dsls[2]), float(dsls[4]), float(dsls[5]), float(dsls[29]), int(dsls[28]), float(dsls[27]), int(dsls[26]), float(dsls[25]), int(dsls[24])))
	# cur.execute("INSERT INTO t_stock_sz000672_bak (price, open_tod, close_lst, high, low, sel_5, sel_5_num, sel_4, sel_4_num, sel_3, sel_3_num, sel_2, sel_2_num, sel_1, sel_1_num, buy_1, buy_1_num, buy_2, buy_2_num, buy_3, buy_3_num, buy_4, buy_4_num, buy_5, buy_5_num) VALUES (%f, %f, %f, %f, %f, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d)" %(float(dsls[3]), float(dsls[1]), float(dsls[2]), float(dsls[4]), float(dsls[5]), float(dsls[29]), int(dsls[28]), float(dsls[27]), int(dsls[26]), float(dsls[25]), int(dsls[24]), float(dsls[23]), int(dsls[22]), float(dsls[21]), int(dsls[20]), float(dsls[11]), int(dsls[10]), float(dsls[13]), int(dsls[12]), float(dsls[15]), int(dsls[14]), float(dsls[17]), int(dsls[16]), float(dsls[19]), int(dsls[20]) ) )
	# cur.execute("INSERT INTO t_stock_sz000672_bak (price, open_tod, close_lst, high, low, sel_5, sel_5_num, sel_4, sel_4_num, sel_3, sel_3_num, sel_2, sel_2_num, sel_1, sel_1_num) VALUES (%f, %f, %f, %f, %f, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d)" %(float(dsls[3]), float(dsls[1]), float(dsls[2]), float(dsls[4]), float(dsls[5]), float(dsls[29]), int(dsls[28]), float(dsls[27]), int(dsls[26]), float(dsls[25]), int(dsls[24]), float(dsls[23]), int(dsls[22]), float(dsls[21]), int(dsls[20]) ) )
	conn.commit()
	# conn.close()
	# print("Success!")

while True:
	reqData(url, dataNum)
	dsls=[]
	time.sleep(1.5)