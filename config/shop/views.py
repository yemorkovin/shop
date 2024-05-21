from django.shortcuts import render
from .models import Product, Banner

def index(request):
    products = Product.objects.all()
    banners = Banner.objects.all()
    return render(request, 'index.html', {'products':products,'banners': banners})

def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products':products})