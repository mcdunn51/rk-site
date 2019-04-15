from django.contrib.auth.models import User
import mysql.connector, csv, pymssql, json, secrets, socket, re, requests

# setting test mode
if socket.gethostname() == 's1.intranet.svg.local':
    test_mode = False
else:
    test_mode = True

# functions
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

# get rid of stupid characters
def sub(string):
    string = str(string).replace("'", "").replace(",", "")
    return  string

# index images 
def imageExists(item):
    try:
        print(item)
        links = {}
        for i in range(0, 9):
            if i == 0:
                link = 'http://images.cdn.rkwltd.com/%s.jpg' % (item)
            else:
                link = 'http://images.cdn.rkwltd.com/%s_0%s.jpg' % (item, i)
            req = requests.get(link)
            if req.status_code == 200:
                links['"image%s"' % (i)] = '"%s"' % (link)
    except:
        pass
    return str(links).replace("'", "")

# update user table
def user(local_conn, local_cur, ref_conn, ref_cur):
    ref_cur.execute("SELECT `email`, `customerNo`, `username` FROM `Contact`")
    res = ref_cur.fetchall()
    for row in res:
        if not User.objects.filter(username=row[2]).exists():
            user=User.objects.create_user(username=row[2], password=secrets.token_urlsafe(), email=row[0])
            user.save()
            local_cur.execute("SELECT id FROM api_userprofile where username = '%s'" % (row[2]))
            if not len(local_cur.fetchall()) > 0:
                if row[1] == 'rep':
                    rep = 1
                else:
                    rep = 0
                local_cur.execute("INSERT INTO `api_userprofile` (`username`, `customerno`, rep) VALUES ('%s', '%s', '%s');" % (row[2], row[1], rep))
                local_conn.commit()

# update customer table
def customer(local_conn, local_cur, ref_conn, ref_cur):
    ref_cur.execute("SELECT `customerCode`, `companyName`, `proforma`, SalespersonCode, ElectricalRep, HousewaresRep, HouseManager, CreditControlManager FROM `Customer`")
    res = ref_cur.fetchall()
    for row in res:
        local_cur.execute("SELECT `customerno` FROM api_userprofile where customerno = '%s'" % (row[0]))
        if len(local_cur.fetchall()) > 0:
            local_cur.execute("UPDATE `api_userprofile` SET `companyName` = '%s', `proforma` = '%s', `billingaddressID` = -1, SalespersonCode = '%s', ElectricalRep = '%s', HousewaresRep = '%s', HouseManager = '%s', CreditControlManager = '%s' WHERE `customerno` = '%s';" % (str(row[1]).replace("'", ""), row[2], row[3], row[4], row[5], row[6], row[7], row[0]))
            local_conn.commit()

# update products table
def products(local_conn, local_cur, ref_conn, ref_cur):
    ref_cur.execute("SELECT `No_`, `CatalogueTheme`, `RRP`, `VolumePrice`, `ManufacturerCode`, `PrimaryColour`, `InventoryPostingGroup`, `ProdName`,`ItemSpec1`, `ItemSpec2`, `ItemSpec3`, `ItemSpec4`, `ItemSpec5`, `ItemSpec6`, `ItemSpec7`, `ItemSpec8`, `ItemSpec9`, `ItemSpec10`, `ReStockDate`, `FreeStock`, `Ti`, `Hi`, `Analysis 2`, `Item Dimensions (H)`, `Item Dimensions (L)`, `Item Dimensions (W)`, `Retail Box Dimensions (H)`, `Retail Box Dimensions (L)`, `Retail Box Dimensions (W)`, `Outer Dimensions (H)`, `Outer Dimensions (L)`, `Outer Dimensions (W)`, `CartonQty`, `PalletQty`, `Electrical or Housewares`, HighSell, Analysis1 from `Items` WHERE `ReStockDate` > '1900-01-01' or freestock > 0")
    res = ref_cur.fetchall()
    for row in res:
        local_cur.execute("SELECT itemno FROM api_product WHERE itemno ='%s'" % (str(row[0])))
        if not len(local_cur.fetchall()) > 0:
            try:
                local_cur.execute("insert into api_product (itemno, CatalogueTheme, RRP, SSP, manufacturerCode, colour, IPG, description, ItemSpec1, ItemSpec2, ItemSpec3, ItemSpec4, ItemSpec5, ItemSpec6, ItemSpec7, ItemSpec8, ItemSpec9, ItemSpec10, restockDate, FreeStock, TI, HI, Analysis2, Item_Height, Item_Length, Item_Width, ProductPaging_Height, ProductPaging_Length, ProductPaging_Width, CartonHeight, CartonLength, CartonWidth, cartonQty, palletQty, `Electrical_or_Housewares`, HighSell, Analysis1) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (row[0], row[1], row[2], row[3], row[4], row[5], str(row[6]).replace('/', ' '), row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36]))
                local_conn.commit()
            except Exception as e:
                print("cant insert '%s' due to '%s'" % (row[0], e))
        else:
            try:
                local_cur.execute("UPDATE api_product SET `CatalogueTheme` = '%s', `RRP` = '%s', `SSP` = '%s', `manufacturerCode` = '%s', `colour` = '%s', `IPG` = '%s', `description` = '%s', `ItemSpec1` = '%s', `ItemSpec2` = '%s', `ItemSpec3` = '%s', `ItemSpec4` = '%s', `ItemSpec5` = '%s', `ItemSpec6` = '%s', `ItemSpec7` = '%s', `ItemSpec8` = '%s', `ItemSpec9` = '%s', `ItemSpec10` = '%s', `restockDate` = '%s', `FreeStock` = '%s', `TI` = '%s', `HI` = '%s', Analysis2 = '%s', `Item_Height` = '%s', `Item_Length` = '%s', `Item_Width` = '%s', `ProductPaging_Height` = '%s', `ProductPaging_Length` = '%s', `ProductPaging_Width` = '%s', `CartonHeight` = '%s', `CartonLength` = '%s', `CartonWidth` = '%s', `cartonQty` = '%s', palletQty = '%s', Electrical_or_Housewares = '%s', HighSell = '%s', Analysis1 = '%s' WHERE `itemno` = '%s'" % (row[1], row[2], row[3], row[4], row[5], str(row[6]).replace('/', ' '), row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[0]))
                local_conn.commit()
            except Exception as e:
                print("cant update '%s' due to '%s'" % (row[0], e))

# update image field on products table
def updateImages(local_conn, local_cur):
    local_cur.execute("select itemno from api_product where restockDate > '1900-01-01' or freestock > 0;")
    for row in local_cur.fetchall():
        images = imageExists(row[0].lower())
        local_cur.execute("update api_product set image = '%s' where itemno = '%s';" % (images, row[0] ))
        local_conn.commit()

# quick update of sto.3ck and restock date
def updateStock(local_conn, local_cur, ref_conn, ref_cur):
    local_cur.execute("SELECT id, itemno FROM api_product where freestock > 0 or restockDate > '1900-01-01'")
    res = local_cur.fetchall()
    for row in res:
        ref_cur.execute("SELECT No_, FreeStock, ReStockDate FROM Items where (freestock > 0 OR ReStockDate > '1900-01-01') and No_ = '%s'" % (row[1])) 
        ref_res = ref_cur.fetchall()
        if not len(ref_res) > 0:
            local_cur.execute("UPDATE api_product SET FreeStock = 0, `restockDate` = '1900-01-01' WHERE id = '%s'" % (row[0])) 
            local_conn.commit()

# update CustomerPrices table
def CustomerPrices(local_conn, local_cur, ref_conn, ref_cur):
    ref_cur.execute("SELECT `customerNo`,`itemno`,`price`,`startDate`,`endDate` FROM `CustomerPrices`")
    res = ref_cur.fetchall()
    for row in res:
        local_cur.execute("SELECT id FROM api_customerprices where customerno = '%s' and itemno = '%s' and price = %s and enddate = '%s' and startdate = '%s';" % (row[0], row[1], row[2], row[4], row[3]))
        if not len(local_cur.fetchall()) > 0:
            local_cur.execute("INSERT INTO `api_customerprices` (`customerNo`, `itemno`, `price`, `endDate`, `startDate`) VALUES ('%s', '%s', '%s', '%s', '%s');" % (row[0], row[1], row[2], row[4], row[3]))
            local_conn.commit()
    local_cur.execute("Delete FROM api_customerprices where endDate < curdate();")
    local_conn.commit()

# update Address table 
def Address(local_cur, local_conn, ref_cur, ref_conn):
    ref_cur.execute("SELECT `customerNO`, `address1`, `address2`, `county`, `postcode`, `phoneNumber`, `country`, `city`, `Type`, `Code` FROM `Address`")
    res = ref_cur.fetchall()
    for row in res:
        local_cur.execute("SELECT * FROM api_address where customerno = '%s' and code = '%s';" % (sub(row[0]), sub(row[9])))
        if len(local_cur.fetchall()) > 0:
            local_cur.execute("UPDATE `api_address` SET `address1` = '%s', `address2` = '%s', `county` = '%s', `postcode` = '%s', `phoneNumber` = '%s', `country` = '%s', `city` = '%s', `Type` = '%s' WHERE customerNO = '%s' and Code = '%s';" % (sub(row[1]), sub(row[2]), sub(row[3]), sub(row[4]), sub(row[5]), sub(row[6]), sub(row[7]), sub(row[8]), sub(row[0]), sub(row[9])))
            local_conn.commit()
        else:
            local_cur.execute("INSERT INTO `api_address` (`customerNO`, `address1`, `address2`, `county`, `postcode`, `phoneNumber`, `country`, `city`, `Type`, Code) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (sub(row[0]), sub(row[1]), sub(row[2]), sub(row[3]), sub(row[4]), sub(row[5]), sub(row[6]), sub(row[7]), sub(row[8]), sub(row[9])))
            local_conn.commit()

# send notificatin if item is now in stock 
def BackinStock(local_cur, local_conn):
    local_cur.execute("SELECT id, customerNO, itemno, notified, dateNotified, username FROM api_backinstock where notified = 0;")
    for row in local_cur.fetchall():
        # email sending code here
        local_cur.execute("UPDATE `api_backinstock` SET `notified` = 1, `dateNotified` = current_timestamp() WHERE `id` = '%s';" % (row[0]))
        local_conn.commit()

# setting variables for db connections
local_conn = create_local_mysql_connection()
local_cur = local_conn.cursor()
ref_conn = create_refrence_mysql_connection()
ref_cur = ref_conn.cursor()

# update function calls
# user(local_conn, local_cur, ref_conn, ref_cur)
# customer(local_conn, local_cur, ref_conn, ref_cur)
# products(local_conn, local_cur, ref_conn, ref_cur)
updateImages(local_conn, local_cur)
# updateStock(local_conn, local_cur, ref_conn, ref_cur)
# CustomerPrices(local_conn, local_cur, ref_conn, ref_cur)
# Address(local_cur, local_conn, ref_cur, ref_conn)
# BackinStock(local_cur, local_conn)