from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    customerID = models.IntegerField()
    customerno = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Product(models.Model):
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
    def __str__(self):
        return self.itemno

class Address(models.Model):
    customerNO = models.IntegerField()
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20) 
    phoneNumber = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)
    def __str__(self):
        return self.address1

class Customer(models.Model):
    customerCode = models.CharField(max_length=20)
    companyName = models.CharField(max_length=50)
    proforma = models.BooleanField()
    billingaddressID = models.IntegerField()
    def __str__(self):
        return self.customerCode

class CustomerPrices(models.Model):
    customerNo = models.CharField(max_length=20)
    itemno = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    startDate = models.DateField()
    endDate = models.DateField()

class Media(models.Model):
    itemno = models.CharField(max_length=100)
    cdn = models.CharField(max_length=20)
    filename = models.CharField(max_length=20)
    def __str__(self):
        return self.filename

class OrderHeader(models.Model):
    customerID = models.IntegerField()
    addressID = models.IntegerField()
    orderDateTime = models.DateTimeField(auto_created=True)
    orderStatus = models.CharField(max_length=20)

class OrderLines(models.Model):
    lineNo = models.IntegerField()
    itemno = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    orderDateTime = models.DateTimeField(auto_created=True)
    orderHeaderID = models.IntegerField()

class Matched(models.Model):
    itemno = models.CharField(max_length=100)
    Matchingitemno = models.IntegerField()
    ParentPartNo = models.CharField(max_length=20)
    MatchingPartNo = models.CharField(max_length=20)