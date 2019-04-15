Front End:

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
        URL: https://5.5.5.10:2087/pma/   it will probably give you an SSL warning, just ignore it. if this doesnt work try below
        https://46.20.231.215:2087/pma

    EndPoints:
        Token:
            http://100.1.253.16:8000/o/token/?grant_type=password&username=Mike&password=tas}Ng2uQ7?!rSS9&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M
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

        OCustomer:
            http://100.1.253.16:8000/OCustomer/
            Params: username
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
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
                    }                ]

        OProductlist:
            http://100.1.253.16:8000/OProductlist/
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
            http://100.1.253.16:8000/OProdDetailed/
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
            http://100.1.253.16:8000/OAddressList/
            Params: customerID
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET
            Returns:
            [
                {
                    "id": 1,
                    "customerID": 1,
                    "address1": "dpw;aiujdoiaw",
                    "address2": "oui8hdoiuawhouih",
                    "town": "oiuhdoiuawhduoiah",
                    "county": "1ouihoiuhoiu",
                    "postcode": "houi",
                    "phoneNumber": "hoiu",
                    "email": "h",
                    "country": "iuoh",
                    "city": "iyg"
                }
            ]

        OOrderHeader:
            http://100.1.253.16:8000/OOrderHeader/
            Params: customerID
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET|POST
            Payload:
                {
                    "customerID": 2,
                    "addressID": 1,
                    "orderDateTime": "1995-02-15T06:00",
                    "orderStatus": "Basket"
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
        
        OOrderLines:
            http://100.1.253.16:8000/OOrderLines/
            Params: customerID
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET|POST
            Payload:
                {
                    "lineNo": 26848,
                    "itemID": 178016,
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
                        "itemID": 178016,
                        "quantity": 5,
                        "price": "23.99",
                        "orderDateTime": "1995-02-25T00:00:00Z",
                        "orderHeaderID": 1
                    }
                ]

        Productlist:
            http://100.1.253.16:8000/Productlist/
            Params: manufacturerCode|itemno|colour|LTFreeStock|GTFreeStock
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET
            Returns:
                [
                    {
                        "id": 1,
                        "itemno": "EGLBUNDLE002",
                        "description": "",
                        "colour": "None",
                        "manufacturerCode": "TOWER",
                        "FreeStock": 12,
                        "restockDate": "1900-01-01"
                ]

        ProdDetailed:
            http://100.1.253.16:8000/ProdDetailed/
            Params: itemno
            Headers:
                Content-Type:application/json
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
                        "FreeStock": 162,
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
                        "CatalogueTheme": ""
                    }
                ]
    
        Manufacturer:
            http://100.1.253.16:8000/Manufacturer/
            Params:
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
            http://100.1.253.16:8000/IPG/
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