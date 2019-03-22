from django.contrib import admin
from .models import Product, Address, Customer, CustomerPrices, Media, OrderHeader, OrderLines

# Register your models here.
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(CustomerPrices)
admin.site.register(Media)
admin.site.register(OrderHeader)
admin.site.register(OrderLines)