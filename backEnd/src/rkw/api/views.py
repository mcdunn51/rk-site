from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework import generics, permissions, filters
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope)
from .models import *
from .serializers import * 

# Oauth views

class OSearch(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.filter(Q(FreeStock__gt = 0) | Q(restockDate__gt = '1900-01-01'))
    serializer_class = OauthProdListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('itemno', 'description', 'colour', 'manufacturerCode', 'IPG', 'Analysis1',)

class OCustomer(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserProfile.objects.all()
    serializer_class = OUserProfileSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',)

class OauthProductlist(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.filter(Q(FreeStock__gt = 0) | Q(restockDate__gt = '1900-01-01'))
    serializer_class = OauthProdListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('manufacturerCode', 'itemno', 'colour', 'IPG')
    def get(self, request, *args, **kwargs):
        LTPrice = self.request.query_params.get('LTPrice', '')
        if LTPrice:
            self.queryset = self.queryset.filter(Price__lte=self.request.query_params['LTPrice'])
        GTPrice = self.request.query_params.get('LTPrice', '')
        if GTPrice:
            self.queryset = self.queryset.filter(Price__gte=self.request.query_params['GTPrice'])
        LTFreeStock = self.request.query_params.get('LTFreeStock', '')
        if LTFreeStock:
            self.queryset = self.queryset.filter(FreeStock__lte=self.request.query_params['LTFreeStock'])
        GTFreeStock = self.request.query_params.get('GTFreeStock', '')
        if GTFreeStock:
            self.queryset = self.queryset.filter(FreeStock__gte=self.request.query_params['GTFreeStock'])
        return super().get(request, *args, **kwargs)

class OauthProdDetailed(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.filter(Q(FreeStock__gt = 0) | Q(restockDate__gt = '1900-01-01'))
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

class OauthOrderHeaderUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderHeader.objects.all()
    serializer_class = OauthOrderHeaderSerializer

class OauthOrderLines(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderLines.objects.all()
    serializer_class = OauthOrderLinesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orderHeaderID',)

class OauthOrderLinesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderLines.objects.all()
    serializer_class = OauthOrderLinesSerializer

class OauthBackInStock(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = BackInStock.objects.all()
    serializer_class = OauthBackInStockSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',)

class OauthBackInStockDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = BackInStock.objects.all()
    serializer_class = OauthBackInStockSerializer

class OBasket(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Basket.objects.all()
    serializer_class = OBasketSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('customerCode',)

class OBasketUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Basket.objects.all()
    serializer_class = OBasketSerializer

# non Oauth views

class Search(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.filter(Q(FreeStock__gt = 0) | Q(restockDate__gt = '1900-01-01'))
    serializer_class = ProdListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('itemno', 'description', 'colour', 'manufacturerCode', 'IPG', 'Analysis1',)

class Productlist(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.filter(Q(FreeStock__gt = 0) | Q(restockDate__gt = '1900-01-01'))
    serializer_class = ProdListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('manufacturerCode', 'itemno', 'colour', 'IPG', 'FreeStock')
    def get_queryset(self):
        LTFreeStock = self.request.query_params.get('LTFreeStock', '')
        if LTFreeStock:
            self.queryset = self.queryset.filter(FreeStock__lte=self.request.query_params['LTFreeStock'])
        GTFreeStock = self.request.query_params.get('GTFreeStock', '')
        if GTFreeStock:
            self.queryset = self.queryset.filter(FreeStock__gte=self.request.query_params['GTFreeStock'])
        return super().get_queryset()
            
class ProdDetailed(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.filter(Q(FreeStock__gt = 0) | Q(restockDate__gt = '1900-01-01'))
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