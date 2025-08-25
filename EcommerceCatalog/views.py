from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

from django.http import HttpResponse
def home(request):
    return HttpResponse ("Welcome to the E-Commerce Catalog")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
# Create your views here.
