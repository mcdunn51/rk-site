from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.mail import send_mail
import mysql.connector, csv, pymssql, json, secrets, socket, re, requests

class update():
    # get rid of stupid characters
    def sub(string):
        string = str(string).replace("'", "").replace(",", "")
        return  string

    # index images
    def imageExists(item, req):
        try:
            links = {}
            for i in range(0, 9):
                if i == 0:
                    link = '%s.jpg' % (item)
                else:
                    link = '%s_0%s.jpg' % (item, i)
                if link in req:
                    links['"image%s"' % (i)] = '"%s"' % (link)
        except:
            pass
        return str(links).replace("'", "")

    # update user table - add code to send alert to user for their username and password HEREMIKE
    def user(local_conn, local_cur, ref_conn, ref_cur):
        ref_cur.execute("SELECT `email`, `customerNo`, `username` FROM `Contact`")
        res = ref_cur.fetchall()
        for row in res:
            username = update.sub(row[2])
            password = secrets.token_urlsafe()
            email = row[0]
            if not User.objects.filter(username=username).exists():
                user=User.objects.create_user(username=username, password=password, email=email)
                user.save()
                # send_mail('Welcome to the RKW website', 'Dear %s, \n \n  Thank you for signing up, feel free to sign in using the below details, where you will be asked to reset your password for security purposes. \n \n  username: %s \n  Password: %s' % (row[2], username, password), 'noreply@rkwltd.com', ['%s' % (row[0])], fail_silently=False,)
                local_cur.execute("SELECT id FROM api_userprofile where username = '%s'" % (username))
                if not len(local_cur.fetchall()) > 0:
                    if row[1] == 'rep':
                        rep = 1
                    else:
                        rep = 0
                    local_cur.execute("INSERT INTO api_userprofile (username, customerno, rep, companyName, proforma, billingaddressID, SalespersonCode, SalespersonCodePhone, SalespersonCodeEmail, ElectricalRep, ElectricalRepPhone, ElectricalRepEmail, HousewaresRep, HousewaresRepPhone, HousewaresRepEmail, HouseManager, HouseManagerPhone, HouseManagerEmail, CreditControlManager, CreditControlManagerPhone, CreditControlManagerEmail) VALUES ('%s', '%s', '%s', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');" % (update.sub(row[2]), row[1], rep))
                    local_conn.commit()

    # update customer table
    def customer(local_conn, local_cur, ref_conn, ref_cur):
        ref_cur.execute("SELECT `customerCode`, `companyName`, `proforma`, SalespersonCode, ElectricalRep, HousewaresRep, HouseManager, CreditControlManager, SalespersonCodePhone, SalespersonCodeEmail, ElectricalRepPhone, ElectricalRepEmail, HousewaresRepPhone, HousewaresRepEmail, HouseManagerPhone, HouseManagerEmail, CreditControlManagerPhone, CreditControlManagerEmail FROM `Customer`")
        res = ref_cur.fetchall()
        for row in res:
            local_cur.execute("SELECT `customerno` FROM api_userprofile where customerno = '%s'" % (row[0]))
            if len(local_cur.fetchall()) > 0:
                local_cur.execute("UPDATE `api_userprofile` SET `companyName` = '%s', `proforma` = '%s', `billingaddressID` = -1, SalespersonCode = '%s', ElectricalRep = '%s', HousewaresRep = '%s', HouseManager = '%s', CreditControlManager = '%s', SalespersonCodePhone = '%s', SalespersonCodeEmail = '%s', ElectricalRepPhone = '%s', ElectricalRepEmail = '%s', HousewaresRepPhone = '%s', HousewaresRepEmail = '%s', HouseManagerPhone = '%s', HouseManagerEmail = '%s', CreditControlManagerPhone = '%s', CreditControlManagerEmail = '%s' WHERE `customerno` = '%s';" % (str(row[1]).replace("'", ""), row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17],row[0]))
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
                    # print("cant insert '%s' due to '%s'" % (row[0], e))
                    pass
            else:
                try:
                    local_cur.execute("UPDATE api_product SET `CatalogueTheme` = '%s', `RRP` = '%s', `SSP` = '%s', `manufacturerCode` = '%s', `colour` = '%s', `IPG` = '%s', `description` = '%s', `ItemSpec1` = '%s', `ItemSpec2` = '%s', `ItemSpec3` = '%s', `ItemSpec4` = '%s', `ItemSpec5` = '%s', `ItemSpec6` = '%s', `ItemSpec7` = '%s', `ItemSpec8` = '%s', `ItemSpec9` = '%s', `ItemSpec10` = '%s', `restockDate` = '%s', `FreeStock` = '%s', `TI` = '%s', `HI` = '%s', Analysis2 = '%s', `Item_Height` = '%s', `Item_Length` = '%s', `Item_Width` = '%s', `ProductPaging_Height` = '%s', `ProductPaging_Length` = '%s', `ProductPaging_Width` = '%s', `CartonHeight` = '%s', `CartonLength` = '%s', `CartonWidth` = '%s', `cartonQty` = '%s', palletQty = '%s', Electrical_or_Housewares = '%s', HighSell = '%s', Analysis1 = '%s' WHERE `itemno` = '%s'" % (row[1], row[2], row[3], row[4], row[5], str(row[6]).replace('/', ' '), row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[0]))
                    local_conn.commit()
                except Exception as e:
                    # print("cant update '%s' due to '%s'" % (row[0], e))
                    pass

    # update image field on products table
    def updateImages(local_conn, local_cur):
        link = 'http://images.cdn.rkwltd.com/'
        req = requests.get(link)
        req = req.text
        local_cur.execute("select itemno from api_product where restockDate > '1900-01-01' or freestock > 0;")
        for row in local_cur.fetchall():
            images = update.imageExists(row[0].lower(), req)
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
            local_cur.execute("SELECT * FROM api_address where customerno = '%s' and code = '%s';" % (update.sub(row[0]), update.sub(row[9])))
            if len(local_cur.fetchall()) > 0:
                local_cur.execute("UPDATE `api_address` SET `address1` = '%s', `address2` = '%s', `county` = '%s', `postcode` = '%s', `phoneNumber` = '%s', `country` = '%s', `city` = '%s', `Type` = '%s' WHERE customerNO = '%s' and Code = '%s';" % (update.sub(row[1]), update.sub(row[2]), update.sub(row[3]), update.sub(row[4]), update.sub(row[5]), update.sub(row[6]), update.sub(row[7]), update.sub(row[8]), update.sub(row[0]), update.sub(row[9])))
                local_conn.commit()
            else:
                local_cur.execute("INSERT INTO `api_address` (`customerNO`, `address1`, `address2`, `county`, `postcode`, `phoneNumber`, `country`, `city`, `Type`, Code) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (update.sub(row[0]), update.sub(row[1]), update.sub(row[2]), update.sub(row[3]), update.sub(row[4]), update.sub(row[5]), update.sub(row[6]), update.sub(row[7]), update.sub(row[8]), update.sub(row[9])))
                local_conn.commit()

    # send notificatin if item is now in stock - needs finsihing off with proper email wording etc HEREMIKE
    def BackinStock(local_cur, local_conn):
        local_cur.execute("SELECT bs.id, bs.itemno, bs.username, (select email from auth_user where username = bs.username), (SELECT `description` FROM `api_product` where itemno = bs.itemno) as email FROM api_backinstock as bs where notified = 0 ;")
        for row in local_cur.fetchall():
            local_cur.execute("SELECT FreeStock FROM api_product where itemno = '%s' and freestock > 0;" % (row[1]))
            if len(local_cur.fetchall()) > 0:
                local_cur.execute("UPDATE `api_backinstock` SET `notified` = 1, `dateNotified` = current_timestamp() WHERE `id` = '%s';" % (row[0]))
                local_conn.commit()
                # set the other line live when it comes to going live, dont want any emails going out to customers while we're deveopling.
                # send_mail('RKW %s is now in Stock' % (row[1]), '%s - %s is now in stock.' % (row[1], row[4]), 'noreply@rkwltd.com', ['%s' % (row[3])], fail_silently=False,)
                send_mail('RKW %s is now in Stock' % (row[1]), '%s - %s is now in stock.' % (row[1], row[4]), 'noreply@rkwltd.com', ['michael.mountford@rkwltd.com'], fail_silently=False,)

    # send notificatin for when users request an account statement
    def AccountStatementRequest(local_cur, local_conn):
        local_cur.execute("SELECT asr.username, (SELECT email FROM auth_user where username = asr.username) as usernameEmail, (SELECT up.CreditControlManager FROM api_userprofile up where username = asr.username) as CreditControlManager, (SELECT up.CreditControlManagerEmail FROM api_userprofile up where username = asr.username) as CreditControlManagerEmail, (SELECT up.customerno FROM api_userprofile up where username = asr.username) as customernon, id from api_accountstatementrequest as asr where notified = 0;")
        for row in local_cur.fetchall():
                # set the other line live when it comes to going live, dont want any emails going out to customers while we're deveopling.
                send_mail("Account Statement Request for %s - %s" % (row[4] ,row[0]), "Hi %s, \n\n Customerno: %s \n Username: %s \n Email: %s \n\n Has requested an account statement." % (row[2], row[4], row[0], row[1]), 'noreply@rkwltd.com', ['%s' % (row[1])], fail_silently=False, )
                send_mail("Account Statement Request for %s - %s" % (row[4] ,row[0]), "Hi %s, \n\n Customerno: %s \n Username: %s \n Email: %s \n\n Has requested an account statement." % (row[2], row[4], row[0], row[1]), 'noreply@rkwltd.com', ['michael.mountford@rkwltd.com'], fail_silently=False, )
                local_cur.execute("UPDATE `api_accountstatementrequest` SET `notified` = 1, `dateNotified` = current_timestamp() WHERE `id` = %s" % (row[5]))
                local_conn.commit()

    # send notification for when users request an account statement
    def InvoiceRequest(local_cur, local_conn):
        local_cur.execute("SELECT ir.username, ir.invoiceNo, (SELECT email FROM auth_user where username = ir.username) as usernameEmail, (SELECT up.CreditControlManager FROM api_userprofile up where username = ir.username) as CreditControlManager, (SELECT up.CreditControlManagerEmail FROM api_userprofile up where username = ir.username) as CreditControlManagerEmail, (SELECT up.customerno FROM api_userprofile up where username = ir.username) as customernon, id FROM api_invoicerequest as ir where notified = 0")
        for row in local_cur.fetchall():
            send_mail("Invoice Request for %s - %s" % (row[5], row[0]), "Hi %s, \n\n Customerno: %s \n Username: %s \n Email: %s \n\n Has requested an invoice for %s." % (row[3], row[5], row[0], row[2], row[1]), 'noreply@rkwltd.com', ['%s' % (row[2])], fail_silently=False,)
            send_mail("Invoice Request for %s - %s" % (row[5], row[0]), "Hi %s, \n\n Customerno: %s \n Username: %s \n Email: %s \n\n Has requested an invoice for %s." % (row[3], row[5], row[0], row[2], row[1]), 'noreply@rkwltd.com', ['michael.mountford@rkwltd.com'], fail_silently=False,)
            local_cur.execute("UPDATE `django-test`.`api_invoicerequest` SET `notified` = 1, `dateNotified` = current_timestamp() WHERE `id` = '%s'" % (row[6]))
            local_conn.commit()

    # main program, runs functions above
    def main():

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

        # setting variables for db connections
        local_conn = create_local_mysql_connection()
        local_cur = local_conn.cursor()
        ref_conn = create_refrence_mysql_connection()
        ref_cur = ref_conn.cursor()

        # function calls
        # print('running user')
        # update.user(local_conn, local_cur, ref_conn, ref_cur)
        # print('running customer')
        # update.customer(local_conn, local_cur, ref_conn, ref_cur)
        # print('running CustomerPrices')
        # update.CustomerPrices(local_conn, local_cur, ref_conn, ref_cur)
        # print('running Address')
        # update.Address(local_cur, local_conn, ref_cur, ref_conn)
        # print('running products')
        # update.updateImages(local_conn, local_cur)
        # print('running updateStock')
        # update.products(local_conn, local_cur, ref_conn, ref_cur)
        # print('running updateImages')
        # update.updateStock(local_conn, local_cur, ref_conn, ref_cur)
        # print('running BackinStock')
        # update.BackinStock(local_cur, local_conn)
        # print('running AccountStatementRequest')
        # update.AccountStatementRequest(local_cur, local_conn)
        print('running AccountStatementRequest')
        update.InvoiceRequest(local_cur, local_conn)
    
class Command(BaseCommand):
    help = 'Refesh data for mysql'
    def handle(self, *args, **options):
        update.main()