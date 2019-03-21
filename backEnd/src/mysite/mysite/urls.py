from django.contrib import admin
from django.urls import include, path
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope, TokenHasScope)
from rest_framework import generics, permissions
from .view import Productlist, Manufacturerlist, AddressList, ProdDetailed, Login
admin.autodiscover()

from oauth2_provider.decorators import protected_resource
from django.views.decorators.csrf import csrf_exempt

@protected_resource()
@csrf_exempt
def my_view(request):
    # An access token is required to get here...
    # ...
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('Productlist/', Productlist.as_view()),
    path('ProductDetailed/', ProdDetailed.as_view()),
    path('Manufacturer/', Manufacturerlist.as_view()),
    path('Address/', AddressList.as_view()),
    path('Login/', my_view)
]