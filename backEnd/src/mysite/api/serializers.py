from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Address

class ProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "price", "colour")

class ProdDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "description2", "price", "colour", "manufacturerCode", "Product_Category", "RRP", "SSP", "FreeStock", "ItemSpec1", "ItemSpec2", "ItemSpec3", "ItemSpec4", "ItemSpec5", "ItemSpec6", "ItemSpec7", "ItemSpec8", "ItemSpec9", "ItemSpec10", "TI", "HI", "Item_Height", "Item_Length", "Item_Width", "ProductPaging_Height", "ProductPaging_Length", "ProductPaging_Width", "CartonHeight", "CartonLength", "CartonWidth", "palletQty", "cartonQty", "restockDate", "IPGID")

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "manufacturerCode")

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("customerID", "address1", "address2", "town", "county", "postcode", "phoneNumber", "email", "country", "city")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("")