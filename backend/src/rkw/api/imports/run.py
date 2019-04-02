import mysql.connector, csv, pymssql, json, socket
from src.rkw.api.imports.imports import products, user, customer, updateUserID, ifNotStillInStock
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

def create_refrence_mysql_connection():
    conn = mysql.connector.connect(
    host="5.5.5.10",
    database='svglrkwl_svgl1',
    port= '3306',
    user="svglrkwl_svglrkR",
    passwd="H61dk0Fa",
    auth_plugin='caching_sha2_password'
    )
    return conn

if test_mode:
    def create_local_mysql_connection():
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="0000",
        database='django-test',
        auth_plugin='caching_sha2_password'
        )
        return conn
else:
    def create_local_mysql_connection():
        conn = mysql.connector.connect(
        host="localhost",
        user="testserv_root",
        passwd="r6KnZEQrWA",
        database='testserv_rkw',
        auth_plugin='caching_sha2_password'
        )
        return conn

# setting variables for db connections
local_conn = create_local_mysql_connection()
local_cur = local_conn.cursor()
ref_conn = create_refrence_mysql_connection()
ref_cur = ref_conn.cursor()
mssql_conn = create_mssql_connection()
mssql_cur = mssql_conn.cursor()

# update function calls
user(local_conn, local_cur, mssql_conn, mssql_cur)
customer(local_conn, local_cur, mssql_conn, mssql_cur)
updateUserID(local_conn, local_cur, mssql_conn, mssql_cur)
products(local_conn, local_cur, ref_conn, ref_cur)
ifNotStillInStock(local_conn, local_cur, ref_conn, ref_cur)