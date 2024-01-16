from django.shortcuts import render


def products(request):
    """ Function to render the products"""
    return render(request, 'products/products.html')
