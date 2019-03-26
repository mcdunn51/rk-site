from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Address, OrderHeader, OrderLines, UserProfile

class OUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "username", "customerID")

class OauthProdDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "description2", "price", "colour", "manufacturerCode", "Product_Category", "RRP", "SSP", "FreeStock", "ItemSpec1", "ItemSpec2", "ItemSpec3", "ItemSpec4", "ItemSpec5", "ItemSpec6", "ItemSpec7", "ItemSpec8", "ItemSpec9", "ItemSpec10", "TI", "HI", "Item_Height", "Item_Length", "Item_Width", "ProductPaging_Height", "ProductPaging_Length", "ProductPaging_Width", "CartonHeight", "CartonLength", "CartonWidth", "palletQty", "cartonQty", "restockDate", "IPGID", "IPG")

class OauthProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "colour", "price", "RRP", "SSP")

class OauthAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', "customerID", "address1", "address2", "town", "county", "postcode", "phoneNumber", "email", "country", "city")

class OauthOrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHeader
        fields = ('id', 'customerID', 'addressID', 'orderDateTime', 'orderStatus')

class OauthOrderLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLines
        fields = ('id', 'lineNo', 'itemID', 'quantity', 'price', 'orderDateTime', 'orderHeaderID')

# non Oauth serializers
class ProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "colour")

class ProdDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "description2", "colour", "manufacturerCode", "Product_Category", "FreeStock", "ItemSpec1", "ItemSpec2", "ItemSpec3", "ItemSpec4", "ItemSpec5", "ItemSpec6", "ItemSpec7", "ItemSpec8", "ItemSpec9", "ItemSpec10", "TI", "HI", "Item_Height", "Item_Length", "Item_Width", "ProductPaging_Height", "ProductPaging_Length", "ProductPaging_Width", "CartonHeight", "CartonLength", "CartonWidth", "palletQty", "cartonQty", "restockDate", "IPGID")

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "manufacturerCode")