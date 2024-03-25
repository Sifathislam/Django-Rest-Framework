from django.shortcuts import render
from . import serializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from . import models
from rest_framework import generics
from . import filter
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.userAccountSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializer.CategorySerializer


class ProductFilterList(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    filterset_class = filter.ProductFilter
    search_fields = ['id','title','price']