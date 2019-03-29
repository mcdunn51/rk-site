from django.contrib.auth.models import User
import mysql.connector, csv, pymssql, json, secrets

# update user table
def user(mysql_conn, mysql_cur, mssql_conn, mssql_cur):
    mssql_cur.execute("SELECT [Web User Account], [On Behalf Of], [Search Name] Name  from SVG$Contact WHERE [Web User Account] <>'' and Name <>'' and [On Behalf Of] <>''")
    res = mssql_cur.fetchall()
    if len(res) > 0:
        for row in res:
            if len(row[2]) > 0:
                if not User.objects.filter(username=row[2]).exists():
                    user=User.objects.create_user(username=row[2], password=secrets.token_urlsafe, email=row[0])
                    user.save()
                    mysql_cur.execute("SELECT id FROM `django-test`.api_userprofile where username = '%s'" % (row[2]))
                    if not len(mysql_cur.fetchall()) > 0:
                        mysql_cur.execute("INSERT INTO `api_userprofile` (`customerID`, `username`, `customerno`) VALUES (-1, '%s', '%s');" % (row[2], row[1]))
                        mysql_conn.commit()

# update customer table
def customer(mysql_conn, mysql_cur, mssql_conn, mssql_cur):
    mysql_cur.execute("SELECT customerno FROM `django-test`.api_userprofile where customerid = '-1';")
    res = mysql_cur.fetchall()
    for row in res:
        mssql_cur.execute("SELECT No_, Name, -1 as proforma, -1 as billingaddressID from SVG$Customer WHERE No_ = '%s'" % (row[0]))
        res = mssql_cur.fetchall()
        if len(res) > 0:
            for row in res:
                mysql_cur.execute("SELECT id FROM `django-test`.api_customer where customercode = '%s'" % (row[0]))
                if not len(mysql_cur.fetchall()) > 0:
                    mysql_cur.execute("INSERT INTO `api_customer` (`customerCode`, `companyName`, `proforma`, `billingaddressID`) VALUES ( '%s', '%s', '%s', '%s')" % (row[0], str(row[1]).replace("'", ""), row[2], row[3]))
                    mysql_conn.commit()

# update user id field         
def updateUserID(mysql_conn, mysql_cur, mssql_conn, mssql_cur):
    mysql_cur.execute("SELECT id, customerno FROM `django-test`.api_userprofile where customerid = -1")
    res = mysql_cur.fetchall()
    for row in res:
        mysql_cur.execute("SELECT id FROM `django-test`.api_customer where customercode = '%s'" % (row[1]))
        checkIfExists = mysql_cur.fetchall()
        if len(checkIfExists) > 0:
            for checkIfExists_line in checkIfExists:
                mysql_cur.execute("UPDATE api_userprofile` SET `customerID` = '%s' WHERE `id` = '%s'" % (checkIfExists_line[0], row[0]))
                mysql_conn.commit()

# update ipg table
def ipg(mysql_conn, mysql_cur, mssql_conn, mssql_cur):
    mssql_cur.execute("SELECT Code, Description, [Electrical or Housewares] from [SVG$Inventory Posting Group]")
    res = mssql_cur.fetchall()
    for row in res:
        if len(row) > 0:
            mysql_cur.execute("SELECT * FROM `django-test`.api_ipg WHERE Code ='%s'" % (str(row[0])))
            checkIfExists = mysql_cur.fetchall()
            if not len(checkIfExists) > 0:
                try:
                    mysql_cur.execute("INSERT INTO `api_ipg` (`Code`, `Description`, `EorH`) VALUES ('%s', '%s', '%s');" % (row[0], row[1], row[2]))
                    mysql_conn.commit()
                except Exception as e:
                    pass

# update products table
def products(mysql_conn, mysql_cur, mssql_conn, mssql_cur):
    mssql_cur.execute("SELECT I.No_, I.Description, I.[Description 2], I.[Unit List Price], I.[Primary Colour], I.[Manufacturer Code], I.[Analysis 2], I.RRP, I.[Volume Price], (100) AS FreeStock, WI.[Item Spec 1], WI.[Item Spec 2], WI.[Item Spec 3], WI.[Item Spec 4], WI.[Item Spec 5], WI.[Item Spec 6], WI.[Item Spec 7], WI.[Item Spec 8], WI.[Item Spec 9], WI.[Item Spec 10], I.Ti, I.Hi, I.[Item Dimensions (H)], I.[Item Dimensions (L)], I.[Item Dimensions (W)], I.[Retail Box Dimensions (H)], I.[Retail Box Dimensions (L)], I.[Retail Box Dimensions (W)], I.[Outer Dimensions (H)], I.[Outer Dimensions (L)],I.[Outer Dimensions (W)], ISNULL((SELECT IUOM.[Qty_ per Unit of Measure] FROM [SVG$Item Unit of Measure] AS IUOM WHERE IUOM.[Item No_] = I.No_ AND IUOM.Code = 'pallet'), 0) AS palletQty, I.[Units per Outer], GETDATE() AS restockDated, I.[Inventory Posting Group] FROM SVG$Item AS I INNER JOIN [SVG$Web Item] AS WI ON I.No_ = WI.[Item Code] WHERE I.[Volume Price] > 0")
    res = mssql_cur.fetchall()
    if len(res) > 0:
        for row in res:
            if len(row) > 0:
                mysql_cur.execute("SELECT * FROM api_product WHERE itemno ='%s'" % (str(row[0])))
                checkIfExists = mysql_cur.fetchall()
                if not len(checkIfExists) > 0:
                    try:
                        mysql_cur.execute("insert into api_product (itemno, description, description2, price, colour, manufacturerCode, Product_Category, RRP, SSP, FreeStock, ItemSpec1, ItemSpec2, ItemSpec3, ItemSpec4, ItemSpec5, ItemSpec6, ItemSpec7, ItemSpec8, ItemSpec9, ItemSpec10, Ti, HI, Item_Height, Item_Length, Item_Width, ProductPaging_Height, ProductPaging_Length, ProductPaging_Width, CartonHeight, CartonLength, CartonWidth, palletQty, cartonQty, restockDate, IPGID, IPG) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', (SELECT ID FROM api_ipg WHERE Code = '%s'), '%s' )" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[34]))
                        mysql_conn.commit()
                    except Exception as e:
                        pass