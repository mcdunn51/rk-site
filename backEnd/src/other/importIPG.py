# import sqlite3, csv

import mysql.connector, csv, pymssql, json
from django.conf import settings

test_mode = True

def create_mssql_connection():
	host = r'navsqlat\RKWL1'
	username = 'MICHAELM'
	password = 'michael91448'
	database = 'SVGL1'
	conn = pymssql.connect(host, username, password, database)
	return  conn

if test_mode:
    def create_mysql_connection():
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="0000",
        database='django-test',
        auth_plugin='caching_sha2_password'
        )
        return conn
else:
    def create_mysql_connection():
        conn = mysql.connector.connect(
        host="localhost",
        user="testserv_root",
        passwd="0000",
        database='testserv_rkw',
        auth_plugin='caching_sha2_password'
        )
        return conn

mysql_conn = create_mysql_connection()
mysql_cur = mysql_conn.cursor()
mssql_conn = create_mssql_connection()
mssql_cur = mssql_conn.cursor()

sql = 'DELETE FROM `django-test`.`api_ipg`'
mysql_cur.execute(sql)
mysql_conn.commit()

sql = "SELECT Code, Description, [Electrical or Housewares] from [SVG$Inventory Posting Group]"
mssql_cur.execute(sql)
res = mssql_cur.fetchall()
for row in res:
    try:
        sql = "INSERT INTO `django-test`.`api_ipg` (`Code`, `Description`, `EorH`) VALUES ('%s', '%s', '%s');" % (row[0], row[1], row[2])
        print(sql)
        mysql_cur.execute(sql)
        mysql_conn.commit()
    except Exception as e:
        print('cant import %s' % (e))