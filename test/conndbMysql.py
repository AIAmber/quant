import MySQLdb

databaseName = 'quant'
username = 'root'
password = 'Bang103.'
host = '120.76.145.62'
port = 3306

# def connDB(databaseName, username, password, host, port):
# 	conn = psycopg2.connect(databaseName, username, password, host, port)

# db = connDB(databaseName, username, password, host, port)
conn = MySQLdb.connect(host=host, port=port, user=username, passwd=password, db=databaseName)
cur = conn.cursor()
cur.execute("INSERT INTO t_test (test_name, test_price, test_total) VALUES ('%s', %f, %d)" %('sfsn', 9.760, 1000))
conn.commit()
conn.close()
print("Success!")