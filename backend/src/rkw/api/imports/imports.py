import mysql.connector, csv, pymssql, json
from django.conf import settings

def IPG(mysql_conn, mysql_cur, mssql_conn, mssql_cur, test_mode):
    if test_mode:
        sql = 'DELETE FROM `django-test`.`api_ipg`'
        mysql_cur.execute(sql)
        mysql_conn.commit()

    sql = "SELECT Code, Description, [Electrical or Housewares] from [SVG$Inventory Posting Group]"
    mssql_cur.execute(sql)
    res = mssql_cur.fetchall()
    if len(res) > 0:
        for row in res:
            # try:
            sql = "INSERT INTO `django-test`.`api_ipg` (`Code`, `Description`, `EorH`) VALUES ('%s', '%s', '%s');" % (row[0], row[1], row[2])
            print(sql)
            mysql_cur.execute(sql)
            mysql_conn.commit()
            # except Exception as e:
            #     print('cant import %s' % (e))

def Products(mysql_conn, mysql_cur, mssql_conn, mssql_cur, test_mode):
    if test_mode:
        sql = 'DELETE FROM `django-test`.`api_product`'
        mysql_cur.execute(sql)
        mysql_conn.commit()

    sql = """SELECT I.No_,
                I.Description,
                I.[Description 2],
                I.[Unit List Price],
                I.[Primary Colour],
                I.[Manufacturer Code],
                I.[Analysis 2],
                I.RRP,
                I.[Volume Price],
                (100) AS FreeStock,
                WI.[Item Spec 1],
                WI.[Item Spec 2],
                WI.[Item Spec 3],
                WI.[Item Spec 4],
                WI.[Item Spec 5],
                WI.[Item Spec 6],
                WI.[Item Spec 7],
                WI.[Item Spec 8],
                WI.[Item Spec 9],
                WI.[Item Spec 10],
                I.Ti,
                I.Hi,
                I.[Item Dimensions (H)],
                I.[Item Dimensions (L)],
                I.[Item Dimensions (W)],
                I.[Retail Box Dimensions (H)],
                I.[Retail Box Dimensions (L)],
                I.[Retail Box Dimensions (W)],
                I.[Outer Dimensions (H)],
                I.[Outer Dimensions (L)],
                I.[Outer Dimensions (W)],
                ISNULL((
                    SELECT IUOM.[Qty_ per Unit of Measure]
                    FROM [SVG$Item Unit of Measure] AS IUOM
                    WHERE IUOM.[Item No_] = I.No_
                        AND IUOM.Code = 'pallet'
                ), 0) AS palletQty,
                I.[Units per Outer],
                GETDATE() AS restockDated,
                I.[Inventory Posting Group]
            FROM SVG$Item AS I
            INNER JOIN [SVG$Web Item] AS WI ON I.No_ = WI.[Item Code]
            WHERE I.[Volume Price] > 0"""
    mssql_cur.execute(sql)
    res = mssql_cur.fetchall()
    for row in res:
        try:
            sql = "insert into `django-test`.api_product (itemno, description, description2, price, colour, manufacturerCode, Product_Category, RRP, SSP, FreeStock, ItemSpec1, ItemSpec2, ItemSpec3, ItemSpec4, ItemSpec5, ItemSpec6, ItemSpec7, ItemSpec8, ItemSpec9, ItemSpec10, Ti, HI, Item_Height, Item_Length, Item_Width, ProductPaging_Height, ProductPaging_Length, ProductPaging_Width, CartonHeight, CartonLength, CartonWidth, palletQty, cartonQty, restockDate, IPGID, IPG) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', (SELECT ID FROM `django-test`.`api_ipg` WHERE Code = '%s'), '%s' )" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[34])
            print(sql)
            mysql_cur.execute(sql)
            mysql_conn.commit()
        except Exception as e:
            print('cant import %s' % (e))