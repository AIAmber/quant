import MySQLdb
import requests
import re
import os
import time

dataNum = 'sz000672'
url = "http://hq.sinajs.cn/list="+dataNum
htmlPwd = "/axebox/code/quant/www/test.html"
ins = 0

todTimeSim = time.strftime('%Y%m%d', time.localtime(time.time()))
# print(todTimeSim)
tableName = 't_stock_sz000672_' + todTimeSim[2:]
with open('./create_msq_text.sql') as f:
	sqlText = f.read()

databaseName = 'test'
username = 'axepolardb'
password = 'Bang103_'
# host = 'axepolardb.mysql.polardb.cnsh.rds.aliyuncs.com'
host = 'pc-uf600zpg677589li5.mysql.polardb.cnsh.rds.aliyuncs.com'
port = 3306


# def connDB(databaseName, username, password, host, port):
# 	conn = psycopg2.connect(databaseName, username, password, host, port)

# db = connDB(databaseName, username, password, host, port)
conn = MySQLdb.connect(host=host, port=port, user=username, passwd=password, db=databaseName)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS %s (%s)" %(tableName, sqlText))
conn.commit()

dsls = []
def reqData(url, dataNum):
	r = requests.get(url)
	# r.status_code
	# print(r.text)
	with open(htmlPwd, 'w') as htmlFile:
		htmlFile.write(r.text)

	stripSlice = "'var hq_str_"+dataNum+"=\""
	dataSlice = r.text.lstrip(stripSlice).split(',')
	# print(dataSlice)
	# dsls = []
	for dsl in dataSlice:
		dsls.append(dsl)
	# print(dsls)

	# dt = reqData(url, dataNum)
	# print(dsls)

	name = 'sz000672'
	volume = int(dsls[8])
	turnVolume = float(dsls[9])
	timeStamp = dsls[30] + ' ' + dsls[31]
	# print(volume, turnVolume, timeStamp)

	cur.execute("INSERT INTO %s (time_stamp ,stock_name, price, open_tod, close_lst, high, low, sel_5, sel_5_num, sel_4, sel_4_num, sel_3, sel_3_num, sel_2, sel_2_num, sel_1, sel_1_num, buy_1, buy_1_num, buy_2, buy_2_num, buy_3, buy_3_num, buy_4, buy_4_num, buy_5, buy_5_num, volume, turn_volume) VALUES ('%s', '%s', %f, %f, %f, %f, %f, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %d, %f)" %(tableName, timeStamp, name, float(dsls[3]), float(dsls[1]), float(dsls[2]), float(dsls[4]), float(dsls[5]), float(dsls[29]), int(dsls[28]), float(dsls[27]), int(dsls[26]), float(dsls[25]), int(dsls[24]), float(dsls[23]), int(dsls[22]), float(dsls[21]), int(dsls[20]), float(dsls[11]), int(dsls[10]), float(dsls[13]), int(dsls[12]), float(dsls[15]), int(dsls[14]), float(dsls[17]), int(dsls[16]), float(dsls[19]), int(dsls[18]), volume, turnVolume ) )

	conn.commit()
	# conn.close()
	# print("Success!")

while ins < 4788:
	reqData(url, dataNum)
	dsls=[]
	time.sleep(1.7)
	ins += 1

exit()