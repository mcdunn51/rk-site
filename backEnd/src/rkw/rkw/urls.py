from django.contrib import admin
from django.urls import include, path
from api.views import *
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    # Oauth paths
    path('OSearch/', OSearch.as_view()),
    path('OCustomer/', OCustomer.as_view()),
    path('OProductlist/', OauthProductlist.as_view()),
    path('OProdDetailed/', OauthProdDetailed.as_view()),
    path('OAddressList/', OauthAddressList.as_view()),
    path('OOrderHeader/', OauthOrderHeader.as_view()),
    path('OOrderHeader/UpdateDelete/<pk>', OauthOrderHeaderUpdateDelete.as_view()),
    path('OOrderLines/', OauthOrderLines.as_view()),
    path('OOrderLines/UpdateDelete/<pk>', OauthOrderLinesUpdateDelete.as_view()),
    path('OBackInStock/', OauthBackInStock.as_view()),
    path('OBackInStock/Delete/<pk>', OauthBackInStockDelete.as_view()),
    path('OBasket/', OBasket.as_view()),
    path('OBasket/UpdateDelete/<pk>', OBasketUpdateDelete.as_view()),
    path('OAccountStatementRequest', OAccountStatementRequest.as_view()),
    path('OInvoiceRequest', OInvoiceRequest.as_view()),
    
    # non Oauth paths
    path('Search/', Search.as_view()),
    path('Productlist/', Productlist.as_view()),
    path('ProductDetailed/', ProdDetailed.as_view()),
    path('Manufacturer/', Manufacturerlist.as_view()),
    path('IPG/', IPG.as_view())
]