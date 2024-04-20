from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import OrderItem
from testimonials.models import Testimonial
from cart.models import OrderItem
from .models import Product


def products(request):
    """ Function to render the products sorted by categorie or users input """
    products = Product.objects.all()

    if 'category' in request.GET:
        category = request.GET['category'].split(',')
        products = Product.objects.filter(Q(category__name__in=category)).all()

    if 'search-input' in request.GET:
        search_input = request.GET.get("search-input")
        products = Product.objects.filter(
            Q(name__icontains=search_input) |
            Q(description__icontains=search_input)).all()

    if 'sort' in request.GET:
        sort_method = request.GET['sort'].split('_')
        if 'price' in sort_method:
            if 'asc' in sort_method:
                products = products.order_by('price').all()
            else:
                products = products.order_by('-price').all()
        if 'rating' in sort_method:
            if 'asc' in sort_method:
                products = products.order_by('-rating').all()
            else:
                products = products.order_by('rating').all()
        if 'name' in sort_method:
            if 'asc' in sort_method:
                products = products.order_by('name').all()
            else:
                products = products.order_by('-name').all()
        if 'category' in sort_method:
            if 'asc' in sort_method:
                products = products.order_by('category').all()
            else:
                products = products.order_by('-category').all()

    context = {"products": products,
               'range': range(1, 6)}

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Function to render the product detail"""
    product = get_object_or_404(Product, id=product_id)
    testimonials = Testimonial.objects.filter(product_id=product_id).all()
    try:
        review_permission = OrderItem.objects.filter(user=request.user).filter(product_id=product_id).all()
        context = {'product': product,
                   'testimonials': testimonials,
                   'review_permission': review_permission,
                   'range': range(1, 6)}
        return render(request, 'products/product_detail.html', context)
    except:
        pass

    context = {'product': product,
               'testimonials': testimonials,
               'range': range(1, 6)}

    return render(request, 'products/product_detail.html', context)
