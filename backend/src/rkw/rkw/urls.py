from django.contrib import admin
from django.urls import include, path
from api.views import Productlist, Manufacturerlist, ProdDetailed, OauthProductlist, OauthProdDetailed, OauthAddressList, OauthOrderHeader, OauthOrderLines, OCustomer, OauthBackInStock, OauthOrderHeaderUpdate, IPG
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    # Oauth paths
    path('OCustomer/', OCustomer.as_view()),
    path('OProductlist/', OauthProductlist.as_view()),
    path('OProdDetailed/', OauthProdDetailed.as_view()),
    path('OAddressList/', OauthAddressList.as_view()),
    path('OOrderHeader/', OauthOrderHeader.as_view()),
    path('OOrderHeaderUpdate/', OauthOrderHeaderUpdate.as_view()),
    path('OOrderLines/', OauthOrderLines.as_view()),
    path('OBackInStock/', OauthBackInStock.as_view()),
    
    # non Oauth paths
    path('Productlist/', Productlist.as_view()),
    path('ProductDetailed/', ProdDetailed.as_view()),
    path('Manufacturer/', Manufacturerlist.as_view()),
    path('IPG/', IPG.as_view())
]