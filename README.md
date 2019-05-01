Back END:
    DevServer:
        Server IP: 100.1.253.16
        Web Panel Login: 
        Domain: testserver.svg.local
        Username: testserv
        Password: vN2zQUsS
        CentOS WebPanel: https://100.1.253.16:2031/pma/
        scl enable rh-python36 bash
    Refrence DB:
        Server: 5.5.5.10
        DBName: svglrkwl_svgl1
        DBUser: svglrkwl_svglrkR
        Password: H61dk0Fa
        URL: https://5.5.5.10:2087/pma/
        https://46.20.231.215:2087/pma
    EndPoints/Views:
        Admin:
            This endpoint gives you access to the Django Site administration which when logged in enables to you to view and edit within the API, AUTHENTICATION AND AUTHORIZATION and DJANGO OAUTH TOOLKIT tables, please note that normal customers will not have access to this, you need “Staff Status” on the user enabled at a minimum just to be able to login, which you would then apply select permissions against the user for them to able to do anything such as “admin| log entry| Can add log entry” or if you have “Super user Status” enabled you have all permissions.
        Token:
            Link: http://100.1.253.16:8000/o/token/
            Example: http://100.1.253.16:8000/o/token/?grant_type=password&username=<inser username>&password=<insert password>&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M
            Client_id: 3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9
            Client_secret: QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M
            Params: grant_type|username|password|client_id|client_secret
            Type:
                POST
            Returns:
                {
                    "access_token": "4YbEdIQdvxWHGnjzX5oVoxKUEfRC9e",
                    "expires_in": 300000,
                    "token_type": "Bearer",
                    "scope": "read write groups",
                    "refresh_token": "LLR3fjm5q556GfiEGdZNoq0sXxGOWY"
                }
        OSearch:
            Link: http://100.1.253.16:8000/OSearch/
            Example: http://100.1.253.16:8000/OSearch/?search=<insert search>
            Params: search
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET
            Returns:
                [
                    {
                        "id": 281,
                        "itemno": "T14001",
                        "description": "HALOGEN LOW FAT AIR FRYER",
                        "colour": "Black",
                        "RRP": "99.99",
                        "SSP": "44.99",
                        "manufacturerCode": "TOWER",
                        "FreeStock": 0,
                        "restockDate": "1900-01-01",
                        "Image": "{\"image0\": \"http://images.cdn.rkwltd.com/t14001.jpg\", \"image2\": \"http://images.cdn.rkwltd.com/t14001_02.jpg\", \"image3\": \"http://images.cdn.rkwltd.com/t14001_03.jpg\", \"image4\": \"http://images.cdn.rkwltd.com/t14001_04.jpg\", \"image5\": \"http://images.cdn.rkwltd.com/t14001_05.jpg\", \"image6\": \"http://images.cdn.rkwltd.com/t14001_06.jpg\", \"image7\": \"http://images.cdn.rkwltd.com/t14001_07.jpg\", \"image8\": \"http://images.cdn.rkwltd.com/t14001_08.jpg\"}"
                    }
                ]
        OCustomer:
            Link: http://100.1.253.16:8000/OCustomer/
            Example: http://100.1.253.16:8000/OCustomer/?username=<inser username>
            Params: username
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Params: username
            Type:
                GET
            Returns:
                [
                    {
                        "id": 7,
                        "username": "YOGI SHAH",
                        "customerno": "MAC02",
                        "companyName": "Macdonalds Discount Stores",
                        "rep": false,
                        "SalespersonCode": "GIANNIA",
                        "ElectricalRep": "GIANNIA",
                        "HousewaresRep": "GIANNIA",
                        "proforma": false,
                        "HouseManager": "ANDREWW",
                        "CreditControlManager": "VICTORIAB"
                    }                
                ]
        OProductlist:
            Link: http://100.1.253.16:8000/OProductlist/
            Example: http://100.1.253.16:8000/OProductlist/?manufacturerCode=<insert manufacturerCode>&itemno=<insert itemno>
            Params: manufacturerCode|itemno|LTPrice|GTPrice|colour|LTFreeStock|GTFreeStock|IPG
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET
            Returns:
                [
                    {
                        "id": 281,
                        "itemno": "T14001",
                        "description": "HALOGEN LOW FAT AIR FRYER",
                        "colour": "Black",
                        "RRP": "99.99",
                        "SSP": "44.99",
                        "manufacturerCode": "TOWER",
                        "FreeStock": 3,
                        "restockDate": "1900-01-01",
                        "Image": "{image0: http://images.cdn.rkwltd.com/t14001.jpg, image2: http://images.cdn.rkwltd.com/t14001_02.jpg, image3: http://images.cdn.rkwltd.com/t14001_03.jpg, image4: http://images.cdn.rkwltd.com/t14001_04.jpg, image5: http://images.cdn.rkwltd.com/t14001_05.jpg, image6: http://images.cdn.rkwltd.com/t14001_06.jpg, image7: http://images.cdn.rkwltd.com/t14001_07.jpg, image8: http://images.cdn.rkwltd.com/t14001_08.jpg}"
                    }
                ]
        OProdDetailed:
            Link: http://100.1.253.16:8000/OProdDetailed/
            Example: http://100.1.253.16:8000/OProdDetailed/?itemno=<insert itemno>
            Params: itemno
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET
            Returns:
                [
                    {
                        "id": 57,
                        "itemno": "SK22110GRN",
                        "description": "Retro Pump Espresso Coffee Machine - Grey",
                        "colour": "Grey",
                        "manufacturerCode": "SWAN",
                        "RRP": "199.99",
                        "SSP": "99.99",
                        "FreeStock": 148,
                        "ItemSpec1": "15 bars of pressure",
                        "ItemSpec2": "1.2 litre detachable water tank",
                        "ItemSpec3": "1 or 2 cups at once",
                        "ItemSpec4": "Die cast boiler",
                        "ItemSpec5": "Steam pressure control",
                        "ItemSpec6": "Can make Espresso Cappuccino Latte Flat white and more",
                        "ItemSpec7": "Removable drip tray",
                        "ItemSpec8": "Retro design",
                        "ItemSpec9": "1100W",
                        "ItemSpec10": "Includes measuring spoon and coffee presser",
                        "TI": 5,
                        "HI": 3,
                        "Item_Height": "31.00",
                        "Item_Length": "28.40",
                        "Item_Width": "19.40",
                        "ProductPaging_Height": "36.70",
                        "ProductPaging_Length": "25.40",
                        "ProductPaging_Width": "33.70",
                        "CartonHeight": "39.20",
                        "CartonLength": "35.50",
                        "CartonWidth": "52.50",
                        "palletQty": 30,
                        "cartonQty": 2,
                        "restockDate": "1900-01-01",
                        "IPG": "COFFEE MAKERS",
                        "CatalogueTheme": "",
                        "Image": "{image0: http://images.cdn.rkwltd.com/sk22110grn.jpg, image2: http://images.cdn.rkwltd.com/sk22110grn_02.jpg, image3: http://images.cdn.rkwltd.com/sk22110grn_03.jpg, image4: http://images.cdn.rkwltd.com/sk22110grn_04.jpg, image5: http://images.cdn.rkwltd.com/sk22110grn_05.jpg, image6: http://images.cdn.rkwltd.com/sk22110grn_06.jpg, image7: http://images.cdn.rkwltd.com/sk22110grn_07.jpg, image8: http://images.cdn.rkwltd.com/sk22110grn_08.jpg}"
                    }
                ]
        OAddressList:
            Link: http://100.1.253.16:8000/OAddressList/
            Example: http://100.1.253.16:8000/OAddressList/?customerNO=<insert customerNO>
            Params: customerNO
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET
            Returns:
                [
                    {
                        "id": 1,
                        "customerNO": "8978864",
                        "address1": "Sutton House",
                        "address2": "Berry Hill Road",
                        "county": "Staffordshire",
                        "postcode": "ST4 2NL",
                        "phoneNumber": "01782 838822",
                        "country": "UK",
                        "city": "Stoke"
                    }
                ]
        OOrderHeader:
            Link: http://100.1.253.16:8000/OOrderHeader/
            Example: http://100.1.253.16:8000/OOrderHeader/?customerCode=<insert customerCode>
            Params: customerCode
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET|POST
            Payload:
                {
                    "customerCode": "ama01",
                    "addressID": 1,
                    "orderStatus": "Order Placed"
                }
            Returns:
                [
                    {
                        "id": 9,
                        "customerID": 2,
                        "addressID": 1,
                        "orderDateTime": "1995-02-15T06:00:00Z",
                        "orderStatus": "Basket"
                    }
                ]
        OOrderHeader/UpdateDelete:
            Link: http://100.1.253.16:8000/OOrderHeader/UpdateDelete/
            Example: http://100.1.253.16:8000/OOrderHeader/UpdateDelete/<insert id>
            Params: pk
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET|PUT|PATCH|DELETE
            Payload:
                {
                    "customerCode": "ide01",
                    "addressID": 5,
                    "orderDateTime": "1995-02-15T06:00",
                    "orderStatus": "Basket"
                }
            Returns:
                {
                    "id": 15,
                    "customerCode": "ama01",
                    "addressID": 1,
                    "orderDateTime": "1995-02-15T06:00:00Z",
                    "orderStatus": "Basket"
                }
        OOrderLines:
            Link: http://100.1.253.16:8000/OOrderLines/
            Example: http://100.1.253.16:8000/OOrderLines/?orderHeaderID=<insert orderHeaderID>
            Params: customerID
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET|POST
            Payload:
                {
                    "lineNo": 26848,
                    "itemno": 178016,
                    "quantity": 5,
                    "price": "23.99",
                    "orderDateTime": "1995-02-25T00:00:00Z",
                    "orderHeaderID": 2
                }
            Returns:
                [
                    {
                        "id": 1,
                        "lineNo": 1,
                        "itemno": "0",
                        "quantity": 5,
                        "price": "23.99",
                        "orderDateTime": "1995-02-25T00:00:00Z",
                        "orderHeaderID": 1
                    }
                ]
        OOrderLines/UpdateDelete:
            Link: http://100.1.253.16:8000/OOrderLines/UpdateDelete/
            Example: http://100.1.253.16:8000/OOrderLines/UpdateDelete/<insert id>
            Params: pk
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET|PUT|PATCH|DELETE
            Payload:
                {
                    "lineNo": 26848,
                    "itemno": "178016",
                    "quantity": 1000,
                    "price": "23.99",
                    "orderDateTime": "1995-02-25T00:00:00Z",
                    "orderHeaderID": 2
                }
            Returns:
                {
                    "id": 1,
                    "itemno": "178016",
                    "quantity": 5,
                    "price": "23.99",
                    "orderDateTime": "2019-04-26T10:07:09.658960Z",
                    "orderHeaderID": 2
                }
        OBackInStock:
            Link: http://100.1.253.16:8000/OBackInStock/
            Example: http://100.1.253.16:8000/OBackInStock/?username=<insert username>
            Params: username
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET|POST
            Payload:
                {
                    "username": "BRITANNIA STADIUM",
                    "customerNO": "ama01",
                    "itemno": "t14001"
                }
            Returns:
                [
                    {
                        "id": 4,
                        "username": "m",
                        "customerNO": "ama01",
                        "itemno": "IDT80044C"
                    }
                ]
        OBackInStock/Delete:
            Link: http://100.1.253.16:8000/OBackInStock/Delete/
            Example: http://100.1.253.16:8000/OBackInStock/Delete/<insert id>
            Params: username
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                DELETE
            Payload:
                {
                    "username": "BRITANNIA STADIUM",
                    "customerNO": "ama01",
                    "itemno": "t14001"
                }
        OBasket:
            Link: http://100.1.253.16:8000/OBasket/
            Example: http://100.1.253.16:8000/OBasket/?customerCode=<insert customerCode>
            Params: customerCode
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET|POST
            Payload:
                {
                    "customerCode": "ama01",
                    "itemno": "t14001",
                    "quantity": "500",
                    "price": "23.99"
                }
            Returns:
                [
                    {
                        "id": 2,
                        "customerCode": "ama01",
                        "itemno": "t14001",
                        "quantity": 1500,
                        "price": "23.99"
                    }
                ]   
        OBasket/UpdateDelete:
            Link: http://100.1.253.16:8000/OBasket/UpdateDelete/
            Example: http://100.1.253.16:8000/OBasket/UpdateDelete/<insert id>
            Params: pk
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET|PUT|PATCH|DELETE
            Payload:
                {
                    "customerCode": "ama01",
                    "itemno": "t14001",
                    "quantity": "1000",
                    "price": "23.99"
                }
            Returns:
                {
                    "id": 2,
                    "customerCode": "ama01",
                    "itemno": "t14001",
                    "quantity": 1500,
                    "price": "23.99"
                }
        Search:
            Link: http://100.1.253.16:8000/Search/
            Example: http://100.1.253.16:8000/Search/?search=<insert search>
            Params: search
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET
            Returns:
                [
                    {
                        "id": 184,
                        "itemno": "SWKA1010BN",
                        "description": "SWAN RETRO Bread Bin Black",
                        "colour": "Black",
                        "manufacturerCode": "SWAN",
                        "FreeStock": 0,
                        "restockDate": "2019-05-19",
                        "Image": "{\"image0\": \"http://images.cdn.rkwltd.com/swka1010bn.jpg\", \"image2\": \"http://images.cdn.rkwltd.com/swka1010bn_02.jpg\"}"
                    }
                ]
        Productlist:
            Link: http://100.1.253.16:8000/Productlist/
            Example: http://100.1.253.16:8000/Productlist/?manufacturerCode=<insert manufacturerCode>&colour=<insert colour>
            Params: manufacturerCode|itemno|colour|LTFreeStock|GTFreeStock
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET
            Returns:
                [
                    {
                        "id": 736,
                        "itemno": "T14001",
                        "description": "HALOGEN LOW FAT AIR FRYER",
                        "colour": "Black",
                        "manufacturerCode": "TOWER",
                        "FreeStock": 3,
                        "restockDate": "1900-01-01",
                        "Image": "{\"image0\": \"http://images.cdn.rkwltd.com/t14001.jpg\", \"image2\": \"http://images.cdn.rkwltd.com/t14001_02.jpg\", \"image3\": \"http://images.cdn.rkwltd.com/t14001_03.jpg\", \"image4\": \"http://images.cdn.rkwltd.com/t14001_04.jpg\", \"image5\": \"http://images.cdn.rkwltd.com/t14001_05.jpg\", \"image6\": \"http://images.cdn.rkwltd.com/t14001_06.jpg\", \"image7\": \"http://images.cdn.rkwltd.com/t14001_07.jpg\", \"image8\": \"http://images.cdn.rkwltd.com/t14001_08.jpg\"}"
                    }
                ]
        ProdDetailed:
            Link: http://100.1.253.16:8000/ProdDetailed/
            Example: http://100.1.253.16:8000/ProdDetailed/?itemno=<insert itemno>
            Params: itemno
            Headers:
                Content-Type:application/json
            Type:
                GET
            Returns:
                [
                    {
                        "id": 736,
                        "itemno": "T14001",
                        "description": "HALOGEN LOW FAT AIR FRYER",
                        "colour": "Black",
                        "manufacturerCode": "TOWER",
                        "FreeStock": 3,
                        "ItemSpec1": "1300W of power uses less energy and cooks 3 times faster",
                        "ItemSpec2": "12 litre bowl with 5L extender ring great for families",
                        "ItemSpec3": "Triple cooking power of halogen / convection and infrared",
                        "ItemSpec4": "Removable glass bowl for easy cleaning and observation",
                        "ItemSpec5": "Cooks food from frozen no thawing time needed",
                        "ItemSpec6": "Halogen heating element heats directly",
                        "ItemSpec7": "Added browning roasting and flavour enhancement",
                        "ItemSpec8": "Convection circulates the air for even heat distribution",
                        "ItemSpec9": "Includes recipe book",
                        "ItemSpec10": "",
                        "TI": 3,
                        "HI": 5,
                        "Item_Height": "32.40",
                        "Item_Length": "32.40",
                        "Item_Width": "39.50",
                        "ProductPaging_Height": "23.10",
                        "ProductPaging_Length": "36.40",
                        "ProductPaging_Width": "36.40",
                        "CartonHeight": "24.60",
                        "CartonLength": "38.20",
                        "CartonWidth": "73.50",
                        "palletQty": 30,
                        "cartonQty": 2,
                        "restockDate": "1900-01-01",
                        "IPG": "AIR FRYERS",
                        "CatalogueTheme": "NONE",
                        "Image": "{\"image0\": \"http://images.cdn.rkwltd.com/t14001.jpg\", \"image2\": \"http://images.cdn.rkwltd.com/t14001_02.jpg\", \"image3\": \"http://images.cdn.rkwltd.com/t14001_03.jpg\", \"image4\": \"http://images.cdn.rkwltd.com/t14001_04.jpg\", \"image5\": \"http://images.cdn.rkwltd.com/t14001_05.jpg\", \"image6\": \"http://images.cdn.rkwltd.com/t14001_06.jpg\", \"image7\": \"http://images.cdn.rkwltd.com/t14001_07.jpg\", \"image8\": \"http://images.cdn.rkwltd.com/t14001_08.jpg\"}"
                    }
                ]
        Manufacturer:
            Link: http://100.1.253.16:8000/Manufacturer/
            Headers:
                Content-Type:application/json
            Type:
                GET
            Returns:
                [
                    {
                        "manufacturerCode": "MORPHY"
                    }
                ]
        IPG:
            Link: http://100.1.253.16:8000/IPG/
            Example: http://100.1.253.16:8000/IPG/?Electrical_or_Housewares=<insert Electrical_or_Housewares>
            Params: Electrical_or_Housewares
            Headers:
                Content-Type:application/json
            Type:
                GET
            Returns:
                [
                    {
                        "IPG": "VACUUM CLEANER BAGS AND ACCESSORIES"
                    }
                ]
    serializers:
        OUserProfileSerializer:
            model = UserProfile
            fields = ("id", "username", "customerno", "companyName", "rep", "proforma", "SalespersonCode", "SalespersonCodePhone", "SalespersonCodeEmail", "ElectricalRep", "ElectricalRepPhone", "ElectricalRepEmail", "HousewaresRep", "HousewaresRepPhone", "HousewaresRepEmail", "HouseManager", "HouseManagerPhone", "HouseManagerEmail", "CreditControlManager", "CreditControlManagerPhone", "CreditControlManagerEmail")
        OauthProdDetailedSerializer:
            model = Product
            fields = ("id", "itemno", "description", "colour", "manufacturerCode", "RRP", "SSP", "FreeStock", "ItemSpec1", "ItemSpec2", "ItemSpec3", "ItemSpec4", "ItemSpec5", "ItemSpec6", "ItemSpec7", "ItemSpec8", "ItemSpec9", "ItemSpec10", "TI", "HI", "Item_Height", "Item_Length", "Item_Width", "ProductPaging_Height", "ProductPaging_Length", "ProductPaging_Width", "CartonHeight", "CartonLength", "CartonWidth", "palletQty", "cartonQty", "restockDate", "IPG", "CatalogueTheme", "Image")
        OauthProdListSerializer:
            model = Product
            fields = ("id", "itemno", "description", "colour", "RRP", "SSP", "manufacturerCode", "FreeStock", "restockDate", "Image")
        OauthAdressSerializer:
            model = Address
            fields = ('id', "customerNO", "address1", "address2", "county", "postcode", "phoneNumber", "country", "city")
        OauthOrderHeaderSerializer:
            model = OrderHeader
            fields = ('id', 'customerCode', 'addressID', 'orderDateTime', 'orderStatus')
        OauthOrderLinesSerializer:
            model = OrderLines
            fields = ('id', 'itemno', 'quantity', 'price', 'orderDateTime', 'orderHeaderID')
        OauthBackInStockSerializer:
            model = BackInStock
            fields = ('id', 'username', 'customerNO', 'itemno')
        OBasketSerializer:
            model = Basket
            fields = ('id', 'customerCode', 'itemno', 'quantity', 'price')
        ProdListSerializer:
            model = Product
            fields = ("id", "itemno", "description", "colour", "manufacturerCode", "FreeStock", "restockDate", "Image")
        ProdDetailedSerializer:
            model = Product
            fields = ("id", "itemno", "description", "colour", "manufacturerCode", "FreeStock", "ItemSpec1", "ItemSpec2", "ItemSpec3", "ItemSpec4", "ItemSpec5", "ItemSpec6", "ItemSpec7", "ItemSpec8", "ItemSpec9", "ItemSpec10", "TI", "HI", "Item_Height", "Item_Length", "Item_Width", "ProductPaging_Height", "ProductPaging_Length", "ProductPaging_Width", "CartonHeight", "CartonLength", "CartonWidth", "palletQty", "cartonQty", "restockDate", "IPG", "CatalogueTheme", "Image")
        ManufacturerSerializer:
            model = Product
            fields = ("id", "manufacturerCode")
        IPGSerializer:
            model = Product
            fields = ("id", "IPG")
    Models:
        UserProfile:
            username = models.CharField(max_length=50)
            customerno = models.CharField(max_length=20)
            rep = models.BooleanField()
            companyName = models.CharField(max_length=50)
            proforma = models.BooleanField()
            billingaddressID = models.IntegerField()
            SalespersonCode = models.CharField(max_length=20)
            SalespersonCodePhone = models.CharField(max_length=30, default='0')
            SalespersonCodeEmail = models.CharField(max_length=80, default='0')
            ElectricalRep = models.CharField(max_length=20)
            ElectricalRepPhone = models.CharField(max_length=20, default='0')
            ElectricalRepEmail = models.CharField(max_length=80, default='0')
            HousewaresRep = models.CharField(max_length=20)
            HousewaresRepPhone = models.CharField(max_length=30, default='0')
            HousewaresRepEmail = models.CharField(max_length=80, default='0')
            HouseManager = models.CharField(max_length=20)
            HouseManagerPhone = models.CharField(max_length=30, default='0')
            HouseManagerEmail = models.CharField(max_length=80, default='0')
            CreditControlManager = models.CharField(max_length=20)
            CreditControlManagerPhone = models.CharField(max_length=30, default='0')
            CreditControlManagerEmail = models.CharField(max_length=80, default='0')
        Product:
            itemno = models.CharField(max_length=100)
            description = models.TextField()
            colour = models.CharField(max_length=100)
            manufacturerCode = models.CharField(max_length = 100)
            RRP = models.DecimalField(max_digits=6, decimal_places=2)
            SSP = models.DecimalField(max_digits=6, decimal_places=2)
            FreeStock = models.IntegerField()
            ItemSpec1 = models.CharField(max_length=100)
            ItemSpec2 = models.CharField(max_length=100)
            ItemSpec3 = models.CharField(max_length=100)
            ItemSpec4 = models.CharField(max_length=100)
            ItemSpec5 = models.CharField(max_length=100)
            ItemSpec6 = models.CharField(max_length=100)
            ItemSpec7 = models.CharField(max_length=100)
            ItemSpec8 = models.CharField(max_length=100)
            ItemSpec9 = models.CharField(max_length=100)
            ItemSpec10 = models.CharField(max_length=100)
            TI = models.IntegerField()
            HI = models.IntegerField()
            Item_Height = models.DecimalField(max_digits=6, decimal_places=2)
            Item_Length = models.DecimalField(max_digits=6, decimal_places=2)
            Item_Width = models.DecimalField(max_digits=6, decimal_places=2)
            ProductPaging_Height = models.DecimalField(max_digits=6, decimal_places=2)
            ProductPaging_Length = models.DecimalField(max_digits=6, decimal_places=2)
            ProductPaging_Width = models.DecimalField(max_digits=6, decimal_places=2)
            CartonHeight = models.DecimalField(max_digits=6, decimal_places=2)
            CartonLength = models.DecimalField(max_digits=6, decimal_places=2)
            CartonWidth = models.DecimalField(max_digits=6, decimal_places=2)
            palletQty = models.IntegerField()
            cartonQty = models.IntegerField()
            restockDate = models.DateField()
            IPG = models.CharField(max_length=100)
            CatalogueTheme = models.CharField(max_length=100)
            Analysis2 = models.CharField(max_length=100)
            Electrical_or_Housewares = models.CharField(max_length=100)
            HighSell = models.DecimalField(max_digits=6, decimal_places=2)
            Analysis1 = models.CharField(max_length=100)
            # Image = JSONField(null=True)
            Image = models.TextField(null=True)
        Address:
            customerNO = models.CharField(max_length=20)
            address1 = models.CharField(max_length=50)
            address2 = models.CharField(max_length=50)
            county = models.CharField(max_length=30)
            postcode = models.CharField(max_length=20) 
            phoneNumber = models.CharField(max_length=30)
            country = models.CharField(max_length=20)
            city = models.CharField(max_length=30)
            Type = models.CharField(max_length=20)
            Code = models.CharField(max_length=20)
        CustomerPrices:
            customerNo = models.CharField(max_length=20)
            itemno = models.CharField(max_length=20)
            price = models.DecimalField(max_digits=6, decimal_places=2)
            startDate = models.DateField()
            endDate = models.DateField()
        OrderHeader:
            customerCode = models.CharField(max_length=20)
            addressID = models.IntegerField()
            orderDateTime = models.DateTimeField(auto_now_add=True)
            orderStatus = models.CharField(max_length=20)
        OrderLines:
            itemno = models.CharField(max_length=100)
            quantity = models.IntegerField()
            price = models.DecimalField(max_digits=6, decimal_places=2)
            orderDateTime = models.DateTimeField(auto_now_add=True)
            orderHeaderID = models.IntegerField()
        Matched:
            itemno = models.CharField(max_length=100)
            Matchingitemno = models.IntegerField()
            ParentPartNo = models.CharField(max_length=20)
            MatchingPartNo = models.CharField(max_length=20)
        BackInStock:
            customerNO = models.CharField(max_length=20)
            itemno = models.CharField(max_length=100)
            notified = models.BooleanField(default=False)
            dateNotified = models.DateTimeField(default='1900-01-01')
            username = models.CharField(max_length=50)
            dateCreated = models.DateTimeField(auto_now_add=True)
        Basket:
            customerCode = models.CharField(max_length=20)
            itemno = models.CharField(max_length=100)
            quantity = models.IntegerField()
            price = models.DecimalField(max_digits=6, decimal_places=2)
            dateCreated = models.DateTimeField(auto_now_add=True)