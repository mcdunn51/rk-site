from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(CustomerPrices)
admin.site.register(Media)
admin.site.register(OrderHeader)
admin.site.register(OrderLines)
admin.site.register(Matched)
admin.site.register(BackInStock)
admin.site.register(Basket)
