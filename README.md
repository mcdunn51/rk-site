Front End:

Back END:
    ServerCommands:
        scl enable rh-python36 bash
    Refrence DB:
        Server: 5.5.5.10
        DBUser: svglrkwl_svglrkR
        DBName: svglrkwl_svgl1
        Password: H61dk0Fa
        URL: https://5.5.5.10:2087/pma/   it will probably give you an SSL warning, just ignore it. if this doesnt work try below
        https://46.20.231.215:2087/pma

    EndPoints:
        Token:
            http://100.1.253.16:8000/o/token/?grant_type=password&username=Mike&password=tas}Ng2uQ7?!rSS9&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M
            Params: grant_type|username|password|client_id|client_secret
            Type:
                POST
            Payload:
            Returns:
                {
                    "access_token": "4YbEdIQdvxWHGnjzX5oVoxKUEfRC9e",
                    "expires_in": 300000,
                    "token_type": "Bearer",
                    "scope": "read write groups",
                    "refresh_token": "LLR3fjm5q556GfiEGdZNoq0sXxGOWY"
                }

        OProductlist:
            http://100.1.253.16:8000/OProductlist/
            Params: manufacturerCode|itemno|LTPrice|GTPrice|colour
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET
            Returns:
                [
                    {
                        "id": 131661,
                        "itemno": "100108",
                        "description": "Evoke Pyramid Kettle Red",
                        "colour": "RED",
                        "price": "32.00",
                        "RRP": "59.99",
                        "SSP": "59.99"
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
                        "id": 104649,
                        "itemno": "T14001",
                        "description": "Halogen Low Fat Air Fryer",
                        "description2": "Black",
                        "price": "29.95",
                        "colour": "BLACK",
                        "manufacturerCode": "TOWER",
                        "Product_Category": "EOL",
                        "RRP": "99.99",
                        "SSP": "44.99",
                        "FreeStock": 100,
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
                        "restockDate": "2019-03-15",
                        "IPGID": -1
                    }
                ]
        OAddressList:
            http://100.1.253.16:8000/OAddressList/
            Params:
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>     
            Type:
                GET
            Returns:
            [
                {
                    "customerID": 8978864,
                    "address1": "Sutton House",
                    "address2": "Berry Hill Road",
                    "town": "Staffordshire",
                    "county": "Staffordshire",
                    "postcode": "ST4 2NL",
                    "phoneNumber": "01782 838822",
                    "email": "rkw@rkwltd.com",
                    "country": "UK",
                    "city": "Stoke"
                }
            ]

        Productlist:
            http://100.1.253.16:8000/Productlist/
            Params: manufacturerCode|itemno|LTPrice|GTPrice|colour
            Headers:
                Content-Type:application/json
                Authorization:Bearer <insert token>
            Type:
                GET
            Returns:
                [
                    {
                        "id": 99906,
                        "itemno": "HBHD01",
                        "description": "Hand Blender Holder Accessory",
                        "colour": "BLACK"
                    }
                ]

        OProdDetailed:
            http://100.1.253.16:8000/OProdDetailed/
            Params: itemno
            Headers:
                Content-Type:application/json
            Type:
                GET
            Returns:
                [
                    {
                        "id": 104649,
                        "itemno": "T14001",
                        "description": "Halogen Low Fat Air Fryer",
                        "description2": "Black",
                        "colour": "BLACK",
                        "manufacturerCode": "TOWER",
                        "Product_Category": "EOL",
                        "FreeStock": 100,
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
                        "restockDate": "2019-03-15",
                        "IPGID": -1
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