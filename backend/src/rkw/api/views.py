from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope)
from .models import Product, Address, OrderHeader, OrderLines, UserProfile, BackInStock
from .serializers import ProdListSerializer, ManufacturerSerializer, OauthAdressSerializer, ProdDetailedSerializer, OauthProdDetailedSerializer, OauthProdListSerializer, OauthOrderHeaderSerializer, OauthOrderLinesSerializer, OUserProfileSerializer, OauthBackInStockSerializer, IPGSerializer

# Oauth views

class OCustomer(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserProfile.objects.all()
    serializer_class = OUserProfileSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',)

class OauthProductlist(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = OauthProdListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('manufacturerCode', 'itemno', 'colour', 'IPG')
    def get(self, request, *args, **kwargs):
        if 'LTPrice' in self.request.query_params:
            if len(self.request.query_params['LTPrice']) > 0:
                self.queryset = self.queryset.filter(price__lte=self.request.query_params['LTPrice'])
        if 'GTPrice' in self.request.query_params:
            if len(self.request.query_params['GTPrice']) > 0:
                self.queryset = self.queryset.filter(price__gte=self.request.query_params['GTPrice'])
        if 'LTFreeStock' in self.request.query_params:
            if len(self.request.query_params['LTFreeStock']) > 0:
                self.queryset = self.queryset.filter(FreeStock__lte=self.request.query_params['LTFreeStock'])
        if 'GTFreeStock' in self.request.query_params:
            if len(self.request.query_params['GTFreeStock']) > 0:
                self.queryset = self.queryset.filter(FreeStock__gte=self.request.query_params['GTFreeStock'])
        return super().get(request, *args, **kwargs)

class OauthProdDetailed(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = OauthProdDetailedSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('itemno',)

class OauthAddressList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Address.objects.all()
    serializer_class = OauthAdressSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('customerNO',)

class OauthOrderHeader(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderHeader.objects.all()
    serializer_class = OauthOrderHeaderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('customerCode',)

# still working on this one
class OauthOrderHeaderUpdate(generics.UpdateAPIView):
    permission_classes = []
    queryset = OrderHeader.objects.all()
    serializer_class = OauthOrderHeaderSerializer

class OauthOrderLines(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderLines.objects.all()
    serializer_class = OauthOrderLinesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orderHeaderID',)

class OauthBackInStock(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = BackInStock.objects.all()
    serializer_class = OauthBackInStockSerializer

class OSearch(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = OauthProdListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('itemno', 'description', 'colour',)

# non Oauth views

class Productlist(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProdListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('manufacturerCode', 'itemno', 'colour', 'IPG')
    def get_queryset(self):
        LTFreeStock = self.request.query_params.get('LTFreeStock', '')
        if LTFreeStock:
            self.queryset = self.queryset.filter(LTFreeStock=self.request.query_params['LTFreeStock'])
        GTFreeStock = self.request.query_params.get('GTFreeStock', '')
        if GTFreeStock:
            self.queryset = self.queryset.filter(GTFreeStock=self.request.query_params['GTFreeStock'])
        return super().get_queryset()
            
class ProdDetailed(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProdDetailedSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('itemno',)

class Manufacturerlist(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.values('manufacturerCode').distinct().order_by('manufacturerCode')
    queryset = queryset.filter(FreeStock__gt = 0)
    serializer_class = ManufacturerSerializer

class IPG(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.values('IPG').distinct().order_by('IPG')
    queryset = queryset.filter(FreeStock__gt = 0)
    serializer_class = IPGSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Electrical_or_Housewares',)

class Search(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProdListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('itemno', 'description', 'colour',)