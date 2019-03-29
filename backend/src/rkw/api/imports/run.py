import mysql.connector, csv, pymssql, json, socket
from src.rkw.api.imports.imports import ipg, products, user, customer, updateUserID
# setting test mode
if socket.gethostname() == 's1.intranet.svg.local':
    test_mode = False
else:
    test_mode = True

# functions
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
        passwd="r6KnZEQrWA",
        database='testserv_rkw',
        auth_plugin='caching_sha2_password'
        )
        return conn

# setting variables for db connections
mysql_conn = create_mysql_connection()
mysql_cur = mysql_conn.cursor()
mssql_conn = create_mssql_connection()
mssql_cur = mssql_conn.cursor()

# update function calls
user(mysql_conn, mysql_cur, mssql_conn, mssql_cur)
customer(mysql_conn, mysql_cur, mssql_conn, mssql_cur)
updateUserID(mysql_conn, mysql_cur, mssql_conn, mssql_cur)
# ipg(mysql_conn, mysql_cur, mssql_conn, mssql_cur)
# products(mysql_conn, mysql_cur, mssql_conn, mssql_cur)