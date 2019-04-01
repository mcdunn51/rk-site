from django.contrib.auth.models import User
import mysql.connector, csv, pymssql, json, secrets

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
                    local_cur.execute("SELECT id FROM `api_userprofile where username = '%s'" % (row[2]))
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

# update ipg table
def ipg(local_conn, local_cur, mssql_conn, mssql_cur):
    mssql_cur.execute("SELECT Code, Description, [Electrical or Housewares] from [SVG$Inventory Posting Group]")
    res = mssql_cur.fetchall()
    for row in res:
        if len(row) > 0:
            local_cur.execute("SELECT * FROM api_ipg WHERE Code ='%s'" % (str(row[0])))
            checkIfExists = local_cur.fetchall()
            if not len(checkIfExists) > 0:
                try:
                    local_cur.execute("INSERT INTO `api_ipg` (`Code`, `Description`, `EorH`) VALUES ('%s', '%s', '%s');" % (row[0], row[1], row[2]))
                    local_conn.commit()
                except Exception as e:
                    pass

# update products table
def products(local_conn, local_cur, ref_conn, ref_cur):
    ref_cur.execute("SELECT `No_`, `CatalogueTheme`, `RRP`, `VolumePrice`, `ManufacturerCode`, `PrimaryColour`, `InventoryPostingGroup`, `ProdName`,`ItemSpec1`, `ItemSpec2`, `ItemSpec3`, `ItemSpec4`, `ItemSpec5`, `ItemSpec6`, `ItemSpec7`, `ItemSpec8`, `ItemSpec9`, `ItemSpec10`, `ReStockDate`, `FreeStock` from Items WHERE `ReStockDate` is not null or `FreeStock` is not null")
    res = ref_cur.fetchall()
    if len(res) > 0:
        for row in res:
            print(row)
            local_cur.execute("SELECT * FROM api_product WHERE itemno ='%s'" % (str(row[0])))
            checkIfExists = local_cur.fetchall()
            if not len(checkIfExists) > 0:
                local_cur.execute("insert into api_product (itemno, CatalogueTheme, RRP, SSP, manufacturerCode, colour, IPG, description, ItemSpec1, ItemSpec2, ItemSpec3, ItemSpec4, ItemSpec5, ItemSpec6, ItemSpec7, ItemSpec8, ItemSpec9, ItemSpec10, restockDate, FreeStock) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s')" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19]))
                local_conn.commit()