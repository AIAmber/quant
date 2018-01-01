import requests
import re
import os
import time
import psycopg2

dataNum = 'sz000672'
url = "http://hq.sinajs.cn/list="+dataNum
htmlPwd = "/axebox/code/quant/www/test.html"
ins = 0

todTimeSim = time.strftime('%Y%m%d', time.localtime(time.time()))
# print(todTimeSim)
tableName = 't_stock_sz000672_' + todTimeSim[2:]
with open('./create_msq_text.sql') as f:
	sqlText = f.read()
	# print(sqlText)

database = 'quant'
user = 'postgres'
password = 'Bang103.'
host = '116.196.111.122'
port = '5432'

# conn = MySQLdb.connect(host=host, port=port, user=username, passwd=password, db=databaseName)
conn = MySQLdb.connect(database=database, user=user, password=password, host=host, port=port)
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

	# Stock - Info
	name = 'sz000672'
	volume = int(dsls[8])
	turnVolume = float(dsls[9])
	timeStamp = dsls[30] + ' ' + dsls[31]
	# print(volume, turnVolume, timeStamp)

	# Info - Real Time
	priceIn = float(dsls[3])
	openIn = float(dsls[1])
	closeIn = float(dsls[2])
	highIn = float(dsls[4])
	lowIn = float(dsls[5])

	sel_5In = float(dsls[29])
	sel_5_numIn = int(dsls[28])
	sel_4In = float(dsls[27])
	sel_4_numIn =int(dsls[26])
	sel_3In = float(dsls[25])
	sel_3_numIn =int(dsls[24])
	sel_2In = float(dsls[23])
	sel_2_numIn =int(dsls[22])
	sel_1In = float(dsls[21])
	sel_1_numIn = int(dsls[20])

	buy_5In = float(dsls[11])
	buy_5_numIn = int(dsls[10])
	buy_4In = float(dsls[13])
	buy_4_numIn = int(dsls[12])
	buy_3In = float(dsls[15])
	buy_3_numIn = int(dsls[14])
	buy_2In = float(dsls[17])
	buy_2_numIn = int(dsls[16])
	buy_1In = float(dsls[19])
	buy_1_numIn = int(dsls[18])


	cur.execute("INSERT INTO %s (time_stamp ,stock_name, price, open_tod, close_lst, high, low, sel_5, sel_5_num, sel_4, sel_4_num, sel_3, sel_3_num, sel_2, sel_2_num, sel_1, sel_1_num, buy_1, buy_1_num, buy_2, buy_2_num, buy_3, buy_3_num, buy_4, buy_4_num, buy_5, buy_5_num, volume, turn_volume) VALUES ('%s', '%s', %f, %f, %f, %f, %f, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %f, %d, %d, %f)" %(tableName, timeStamp, name, priceIn, openIn, closeIn, highIn, lowIn, sel_5In, sel_5_numIn, sel_4In, sel_4_numIn, sel_3In, sel_3_numIn, sel_2In, sel_2_numIn, sel_1In, sel_1_numIn, buy_1In, buy_1_numIn, buy_2In, buy_2_numIn, buy_3In, buy_3_numIn, buy_4In, buy_4_numIn, buy_5In, buy_5_numIn , volume, turnVolume ) )

	conn.commit()
	# conn.close()
	# print("Success!")

while ins < 4788:
	reqData(url, dataNum)
	dsls=[]
	time.sleep(1.7)
	ins += 1

exit()