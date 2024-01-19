from django.shortcuts import render
from .models import Product


def products(request):
    """ Function to render the products"""
    products = Product.objects.all()
    context = {"products": products,
               'range': range(1, 6)}
    return render(request, 'products/products.html', context)
