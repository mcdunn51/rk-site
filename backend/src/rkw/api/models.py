from django.db import models

# Create your models here.

class Product(models.Model):
    itemno = models.CharField(max_length=120)
    description = models.TextField()
    description2 = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    colour = models.CharField(max_length=50)
    manufacturerCode = models.CharField(max_length = 50)
    Product_Category = models.CharField(max_length=20)
    RRP = models.DecimalField(max_digits=6, decimal_places=2)
    SSP = models.DecimalField(max_digits=6, decimal_places=2)
    FreeStock = models.IntegerField()
    ItemSpec1 = models.CharField(max_length=69)
    ItemSpec2 = models.CharField(max_length=69)
    ItemSpec3 = models.CharField(max_length=69)
    ItemSpec4 = models.CharField(max_length=69)
    ItemSpec5 = models.CharField(max_length=69)
    ItemSpec6 = models.CharField(max_length=69)
    ItemSpec7 = models.CharField(max_length=69)
    ItemSpec8 = models.CharField(max_length=69)
    ItemSpec9 = models.CharField(max_length=69)
    ItemSpec10 = models.CharField(max_length=69)
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
    IPGID = models.IntegerField()
    def __str__(self):
        return self.itemno

class Address(models.Model):
    customerID = models.IntegerField()
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20) 
    phoneNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.address1

class Customer(models.Model):
    customerCode = models.CharField(max_length=20)
    companyName = models.CharField(max_length=20)
    proforma = models.BooleanField()
    billingaddressID = models.IntegerField()
    def __str__(self):
        return self.customerCode

class CustomerPrices(models.Model):
    salesType = models.CharField(max_length=20)
    customerID = models.IntegerField()
    itemID = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    startDate = models.DateField(),
    endDate = models.DateField()

class Media(models.Model):
    itemID = models.IntegerField()
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
    itemID = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class IPG(models.Model):
    Code = models.CharField(max_length=20)
    Description = models.CharField(max_length=50)
    EorH = models.CharField(max_length=10)

class Matched(models.Model):
    ItemID = models.IntegerField()
    MatchingItemID = models.IntegerField()
    ParentPartNo = models.CharField(max_length=20)
    MatchingPartNo = models.CharField(max_length=20)