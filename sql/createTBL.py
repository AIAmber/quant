import psycopg2

databaseName = 'pypostgres'
username = 'leolee'
password = 'Bang103.'
host = 'localhost'
port = '5432'

# def connDB(databaseName, username, password, host, port):
# 	conn = psycopg2.connect(databaseName, username, password, host, port)

# db = connDB(databaseName, username, password, host, port)
conn = psycopg2.connect(database='quant', user='postgres', password='Bang103.', host='localhost', port='5432')
cur = conn.cursor()
cur.execute("INSERT INTO t_test_name (name) VALUES ('%s')")
conn.commit()
conn.close()
print("Success!")
# print("Sus")