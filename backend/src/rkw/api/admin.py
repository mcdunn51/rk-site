from django.contrib import admin
from .models import Product, Address, Customer, CustomerPrices, Media, OrderHeader, OrderLines, UserProfile, IPG

# Register your models here.
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(CustomerPrices)
admin.site.register(Media)
admin.site.register(OrderHeader)
admin.site.register(OrderLines)
admin.site.register(UserProfile)
admin.site.register(IPG)