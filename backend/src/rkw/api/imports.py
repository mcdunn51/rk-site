from django.contrib.auth.models import User
import mysql.connector, csv, pymssql, json, secrets, socket

# setting test mode
if socket.gethostname() == 's1.intranet.svg.local':
    test_mode = False
else:
    test_mode = True

# functions
def create_mssql_connection():
	conn = pymssql.connect(r'navsqlat\RKWL1', 'MICHAELM', 'michael91448', 'SVGL1')
	return  conn

def create_refrence_mysql_connection():
    conn = mysql.connector.connect(host="5.5.5.10", database='svglrkwl_svgl1', port='3306',user="svglrkwl_svglrkR", passwd="H61dk0Fa", auth_plugin='caching_sha2_password')
    return conn

if test_mode:
    def create_local_mysql_connection():
        conn = mysql.connector.connect(host="localhost", user="root", passwd="0000", database='django-test', auth_plugin='caching_sha2_password')
        return conn
else:
    def create_local_mysql_connection():
        conn = mysql.connector.connect(host="localhost", user="testserv_root", passwd="0000", database='testserv_rkw', auth_plugin='caching_sha2_password')
        return conn

# update user table
def user(local_conn, local_cur, mssql_conn, mssql_cur):
    mssql_cur.execute("SELECT [Web User Account], [On Behalf Of], [Search Name] Name  from SVG$Contact WHERE [Web User Account] <>'' and Name <>'' and [On Behalf Of] <>''")
    res = mssql_cur.fetchall()
    if len(res) > 0:
        for row in res:
            if len(row[2]) > 0:
                if not User.objects.filter(username=row[2]).exists():
                    user=User.objects.create_user(username=row[2], password=secrets.token_urlsafe, email=row[0])
                    user.save()
                    local_cur.execute("SELECT id FROM api_userprofile where username = '%s'" % (row[2]))
                    if not len(local_cur.fetchall()) > 0:
                        local_cur.execute("INSERT INTO `api_userprofile` (`customerID`, `username`, `customerno`) VALUES (-1, '%s', '%s');" % (row[2], row[1]))
                        local_conn.commit()

# update customer table
def customer(local_conn, local_cur, mssql_conn, mssql_cur):
    local_cur.execute("SELECT customerno FROM api_userprofile where customerid = '-1';")
    res = local_cur.fetchall()
    for row in res:
        mssql_cur.execute("SELECT No_, Name, -1 as proforma, -1 as billingaddressID from SVG$Customer WHERE No_ = '%s'" % (row[0]))
        res = mssql_cur.fetchall()
        if len(res) > 0:
            for row in res:
                local_cur.execute("SELECT id FROM api_customer where customercode = '%s'" % (row[0]))
                if not len(local_cur.fetchall()) > 0:
                    local_cur.execute("INSERT INTO api_customer (`customerCode`, `companyName`, `proforma`, `billingaddressID`) VALUES ( '%s', '%s', '%s', '%s')" % (row[0], str(row[1]).replace("'", ""), row[2], row[3]))
                    local_conn.commit()

# update user id field         
def updateUserID(local_conn, local_cur, mssql_conn, mssql_cur):
    local_cur.execute("SELECT id, customerno FROM api_userprofile where customerid = -1")
    res = local_cur.fetchall()
    for row in res:
        local_cur.execute("SELECT id FROM api_customer where customercode = '%s'" % (row[1]))
        checkIfExists = local_cur.fetchall()
        if len(checkIfExists) > 0:
            for checkIfExists_line in checkIfExists:
                local_cur.execute("UPDATE api_userprofile SET `customerID` = '%s' WHERE `id` = '%s'" % (checkIfExists_line[0], row[0]))
                local_conn.commit()

# update products table
def products(local_conn, local_cur, ref_conn, ref_cur):
    ref_cur.execute("SELECT `No_`, `CatalogueTheme`, `RRP`, `VolumePrice`, `ManufacturerCode`, `PrimaryColour`, `InventoryPostingGroup`, `ProdName`,`ItemSpec1`, `ItemSpec2`, `ItemSpec3`, `ItemSpec4`, `ItemSpec5`, `ItemSpec6`, `ItemSpec7`, `ItemSpec8`, `ItemSpec9`, `ItemSpec10`, `ReStockDate`, `FreeStock` from Items WHERE `ReStockDate` > '1900-01-01' or `FreeStock` is not null")
    res = ref_cur.fetchall()
    if len(res) > 0:
        for row in res:
            local_cur.execute("SELECT * FROM api_product WHERE itemno ='%s'" % (str(row[0])))
            checkIfExists = local_cur.fetchall()
            if not len(checkIfExists) > 0:
                local_cur.execute("insert into api_product (itemno, CatalogueTheme, RRP, SSP, manufacturerCode, colour, IPG, description, ItemSpec1, ItemSpec2, ItemSpec3, ItemSpec4, ItemSpec5, ItemSpec6, ItemSpec7, ItemSpec8, ItemSpec9, ItemSpec10, restockDate, FreeStock, TI, HI, Item_Height, Item_Length, Item_Width, ProductPaging_Height, ProductPaging_Length, ProductPaging_Width, CartonHeight, CartonLength, CartonWidth, palletQty, cartonQty) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19]))
                local_conn.commit()
            else:
                try:
                    local_cur.execute("UPDATE api_product SET `description` = '%s', `colour` = '%s', `manufacturerCode` = '%s', `RRP` = '%s', `SSP` = '%s', `FreeStock` = '%s', `ItemSpec1` = '%s', `ItemSpec2` = '%s', `ItemSpec3` = '%s', `ItemSpec4` = '%s', `ItemSpec5` = '%s', `ItemSpec6` = '%s', `ItemSpec7` = '%s', `ItemSpec8` = '%s', `ItemSpec9` = '%s', `ItemSpec10` = '%s', `TI` = 0, `HI` = 0, `Item_Height` = 0, `Item_Length` = 0, `Item_Width` = 0, `ProductPaging_Height` = 0, `ProductPaging_Length` = 0, `ProductPaging_Width` = 0, `CartonHeight` = 0, `CartonLength` = 0, `CartonWidth` = 0, `palletQty` = 0, `cartonQty` = 0, `restockDate` = '%s', `IPG` = '%s', `CatalogueTheme` = '%s' WHERE `itemno` = '%s'" % (row[7], row[5], row[4], row[2], row[3], row[19], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[6], row[1], row[0]))
                    local_conn.commit()
                except:
                    pass
                
# quick update of stock and restock date
def ifNotStillInStock(local_conn, local_cur, ref_conn, ref_cur):
    local_cur.execute("SELECT id, itemno FROM api_product where freestock > 0 or restockDate > '1900-01-01'")
    res = local_cur.fetchall()
    if len(res) > 0:
        for row in res:
            ref_cur.execute("SELECT No_, FreeStock, ReStockDate FROM Items where (freestock is not null OR ReStockDate > '1900-01-01') and No_ = '%s'" % (row[1])) 
            ref_res = ref_cur.fetchall()
            if not len(ref_res) > 0:
                local_cur.execute("UPDATE api_product SET FreeStock = 0, `restockDate` = '1900-01-01' WHERE id = '%s'" % (row[0])) 
                local_conn.commit()

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