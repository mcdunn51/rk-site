from rest_framework import serializers
from .models import *

class OUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "username", "customerno", "companyName", "rep", "proforma", "SalespersonCode", "SalespersonCodePhone", "SalespersonCodeEmail", "ElectricalRep", "ElectricalRepPhone", "ElectricalRepEmail", "HousewaresRep", "HousewaresRepPhone", "HousewaresRepEmail", "HouseManager", "HouseManagerPhone", "HouseManagerEmail" "CreditControlManager", "CreditControlManagerPhone", "CreditControlManagerEmail")

class OauthProdDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "colour", "manufacturerCode", "RRP", "SSP", "FreeStock", "ItemSpec1", "ItemSpec2", "ItemSpec3", "ItemSpec4", "ItemSpec5", "ItemSpec6", "ItemSpec7", "ItemSpec8", "ItemSpec9", "ItemSpec10", "TI", "HI", "Item_Height", "Item_Length", "Item_Width", "ProductPaging_Height", "ProductPaging_Length", "ProductPaging_Width", "CartonHeight", "CartonLength", "CartonWidth", "palletQty", "cartonQty", "restockDate", "IPG", "CatalogueTheme", "Image")

class OauthProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "colour", "RRP", "SSP", "manufacturerCode", "FreeStock", "restockDate", "Image")

class OauthAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', "customerNO", "address1", "address2", "county", "postcode", "phoneNumber", "country", "city")

class OauthOrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHeader
        fields = ('id', 'customerCode', 'addressID', 'orderDateTime', 'orderStatus')

class OauthOrderLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLines
        fields = ('id', 'itemno', 'quantity', 'price', 'orderDateTime', 'orderHeaderID')
    
class OauthBackInStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackInStock
        fields = ('id', 'username', 'customerNO', 'itemno')

class OBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id', 'customerCode', 'itemno', 'quantity', 'price')

# non Oauth serializers
class ProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "colour", "manufacturerCode", "FreeStock", "restockDate", "Image")

class ProdDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "colour", "manufacturerCode", "FreeStock", "ItemSpec1", "ItemSpec2", "ItemSpec3", "ItemSpec4", "ItemSpec5", "ItemSpec6", "ItemSpec7", "ItemSpec8", "ItemSpec9", "ItemSpec10", "TI", "HI", "Item_Height", "Item_Length", "Item_Width", "ProductPaging_Height", "ProductPaging_Length", "ProductPaging_Width", "CartonHeight", "CartonLength", "CartonWidth", "palletQty", "cartonQty", "restockDate", "IPG", "CatalogueTheme", "Image")

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "manufacturerCode")
    
class IPGSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "IPG")

