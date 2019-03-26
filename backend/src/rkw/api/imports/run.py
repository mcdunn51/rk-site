import mysql.connector, csv, pymssql, json
from django.conf import settings
from imports import IPG, Products

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

IPG(mysql_conn, mysql_cur, mssql_conn, mssql_cur, test_mode)
Products(mysql_conn, mysql_cur, mssql_conn, mssql_cur, test_mode)