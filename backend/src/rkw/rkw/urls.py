from django.contrib import admin
from django.urls import include, path
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope, TokenHasScope)
from rest_framework import generics, permissions
from api.views import Productlist, Manufacturerlist, ProdDetailed, OauthProductlist, OauthProdDetailed, OauthAddressList, OauthOrderHeader
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    # Oauth paths
    path('OProductlist/', OauthProductlist.as_view()),
    path('OProdDetailed/', OauthProdDetailed.as_view()),
    path('OAddressList/', OauthAddressList.as_view()),
    path('OOrderHeader/', OauthOrderHeader.as_view()),
    
    # non Oauth paths
    path('Productlist/', Productlist.as_view()),
    path('ProductDetailed/', ProdDetailed.as_view()),
    path('Manufacturer/', Manufacturerlist.as_view()),
]