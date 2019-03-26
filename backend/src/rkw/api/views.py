from django.contrib.auth.models import User
from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope)
from .models import Product, Address, OrderHeader, OrderLines, UserProfile
from .serializers import ProdListSerializer, ManufacturerSerializer, OauthAdressSerializer, ProdDetailedSerializer, OauthProdDetailedSerializer, OauthProdListSerializer, OauthOrderHeaderSerializer, OauthOrderLinesSerializer, OUserProfileSerializer

# Oauth views

class OCustomerID(generics.ListAPIView):
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
        if 'customerID' in self.request.query_params:
            if len(self.request.query_params['customerID']) > 0:
                self.queryset = self.queryset.filter(customerID=self.request.query_params['customerID'])
        return super().get(request, *args, **kwargs)

class OauthOrderHeader(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderHeader.objects.all()
    serializer_class = OauthOrderHeaderSerializer
    def get(self, request, *args, **kwargs):
        if 'customerID' in self.request.query_params:
            if len(self.request.query_params['customerID']) > 0:
                self.queryset = self.queryset.filter(customerID=self.request.query_params['customerID'])
        return super().get(request, *args, **kwargs)

class OauthOrderLines(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = OrderLines.objects.all()
    serializer_class = OauthOrderLinesSerializer
    def get(self, request, *args, **kwargs):
        if 'orderHeaderID' in self.request.query_params:
            if len(self.request.query_params['orderHeaderID']) > 0:
                self.queryset = self.queryset.filter(orderHeaderID=self.request.query_params['orderHeaderID'])
        return super().get(request, *args, **kwargs)

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
    queryset = Product.objects.values('manufacturerCode').distinct()
    serializer_class = ManufacturerSerializer