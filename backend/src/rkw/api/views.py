from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope)
from .models import Product, Address, OrderHeader, OrderLines, UserProfile, BackInStock
from .serializers import ProdListSerializer, ManufacturerSerializer, OauthAdressSerializer, ProdDetailedSerializer, OauthProdDetailedSerializer, OauthProdListSerializer, OauthOrderHeaderSerializer, OauthOrderLinesSerializer, OUserProfileSerializer, OauthBackInStockSerializer, IPGSerializer

# Oauth views

class OCustomerno(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserProfile.objects.all()
    serializer_class = OUserProfileSerializer

class OauthProductlist(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = OauthProdListSerializer
    def get(self, request, *args, **kwargs):
        if 'itemno' in self.request.query_params:
            if len(self.request.query_params['itemno']) > 0:
                self.queryset = self.queryset.filter(itemno=self.request.query_params['itemno'])
        if 'manufacturerCode' in self.request.query_params:
            if len(self.request.query_params['manufacturerCode']) > 0:
                self.queryset = self.queryset.filter(manufacturerCode=self.request.query_params['manufacturerCode'])
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
        if 'colour' in self.request.query_params:
            if len(self.request.query_params['colour']) > 0:
                self.queryset = self.queryset.filter(colour=self.request.query_params['colour'])
        return super().get(request, *args, **kwargs)

class OauthProdDetailed(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = OauthProdDetailedSerializer
    def get(self, request, *args, **kwargs):
        if 'itemno' in self.request.query_params:
            if len(self.request.query_params['itemno']) > 0:
                self.queryset = self.queryset.filter(itemno=self.request.query_params['itemno'])
        return super().get(request, *args, **kwargs)

class OauthAddressList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Address.objects.all()
    serializer_class = OauthAdressSerializer
    def get(self, request, *args, **kwargs):
        if 'customerNO' in self.request.query_params:
            if len(self.request.query_params['customerNO']) > 0:
                self.queryset = self.queryset.filter(customerNO=self.request.query_params['customerNO'])
        return super().get(request, *args, **kwargs)

class OauthOrderHeader(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderHeader.objects.all()
    serializer_class = OauthOrderHeaderSerializer
    def get(self, request, *args, **kwargs):
        if 'customerCode' in self.request.query_params:
            if len(self.request.query_params['customerCode']) > 0:
                self.queryset = self.queryset.filter(customerCode=self.request.query_params['customerCode'])
        return super().get(request, *args, **kwargs)

class OauthOrderHeaderUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderHeader.objects.all()
    serializer_class = OauthOrderHeaderSerializer

class OauthOrderLines(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderLines.objects.all()
    serializer_class = OauthOrderLinesSerializer
    def get(self, request, *args, **kwargs):
        if 'orderHeaderID' in self.request.query_params:
            if len(self.request.query_params['orderHeaderID']) > 0:
                self.queryset = self.queryset.filter(orderHeaderID=self.request.query_params['orderHeaderID'])
        return super().get(request, *args, **kwargs)

class OauthBackInStock(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = BackInStock.objects.all()
    serializer_class = OauthBackInStockSerializer

# non Oauth views

class Productlist(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProdListSerializer
    def get(self, request, *args, **kwargs):
        if 'manufacturerCode' in self.request.query_params:
            if len(self.request.query_params['manufacturerCode']) > 0:
                self.queryset = self.queryset.filter(manufacturerCode=self.request.query_params['manufacturerCode'])
        if 'itemno' in self.request.query_params:
            if len(self.request.query_params['itemno']) > 0:
                self.queryset = self.queryset.filter(itemno=self.request.query_params['itemno'])
        if 'colour' in self.request.query_params:
            if len(self.request.query_params['colour']) > 0:
                self.queryset = self.queryset.filter(colour=self.request.query_params['colour'])
        if 'IPG' in self.request.query_params:
            if len(self.request.query_params['IPG']) > 0:
                self.queryset = self.queryset.filter(IPG=self.request.query_params['IPG'])
        if 'LTFreeStock' in self.request.query_params:
            if len(self.request.query_params['LTFreeStock']) > 0:
                self.queryset = self.queryset.filter(FreeStock__lte=self.request.query_params['LTFreeStock'])
        if 'GTFreeStock' in self.request.query_params:
            if len(self.request.query_params['GTFreeStock']) > 0:
                self.queryset = self.queryset.filter(FreeStock__gte=self.request.query_params['GTFreeStock'])
        return super().get(request, *args, **kwargs)
    
class ProdDetailed(generics.ListAPIView):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProdDetailedSerializer
    def get(self, request, *args, **kwargs):
        if 'itemno' in self.request.query_params:
            if len(self.request.query_params['itemno']) > 0:
                self.queryset = self.queryset.filter(itemno=self.request.query_params['itemno'])
        return super().get(request, *args, **kwargs)

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
    def get(self, request, *args, **kwargs):
        if 'Electrical_or_Housewares' in self.request.query_params:
            if len(self.request.query_params['Electrical_or_Housewares']) > 0:
                self.queryset = self.queryset.filter(Electrical_or_Housewares=self.request.query_params['Electrical_or_Housewares'])
        return super().get(request, *args, **kwargs)