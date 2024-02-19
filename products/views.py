from django.shortcuts import render, get_object_or_404, redirect
from cart.models import OrderItem
from .models import Product, UserRate, Testimonial
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from decimal import Decimal

def products(request):
    """ Function to render the products sorted by categorie or users input"""
    products = Product.objects.all()
    categories = None

    if 'category' in request.GET:
        category = request.GET['category'].split(',')
        products = Product.objects.filter(Q(category__name__in=category)).all()
        # categories = Category.objects.filter(name__in=category).values()

    if 'search-input' in request.GET:
        search_input = request.GET.get("search-input")
        products = Product.objects.filter(Q(name__icontains=search_input) |Q(description__icontains=search_input)).all()

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
    review_permission = OrderItem.objects.filter(user=request.user).filter(product_id=product_id).all()
    context = {"product": product,
               'testimonials': testimonials,
               'review_permission': review_permission,
               'range': range(1, 6)}
    return render(request, 'products/product_detail.html', context)

@login_required
def testimonial(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        user_rating = Decimal(request.POST['rate'])
        user_testimonial = request.POST['testimonial']

        if not (UserRate.objects.filter(user=request.user)
                .filter(product_id=product_id).exists()):
            user_rate = UserRate(
                        user=request.user,
                        rating=user_rating,
                        product=product)
            user_rate.save()
            Product.update_rating(product, user_rating)
        if not (Testimonial.objects.filter(user=request.user)
                .filter(product_id=product_id).exists()):
            testimonial_text = Testimonial(
                            user=request.user,
                            testimonial_text=user_testimonial,
                            product=product)
            testimonial_text.save()
        return redirect("product_detail", product_id)

    return redirect("product_detail", product_id)



def edit_testimonial(request, product_id):
    """ Function to render the edit testimonial"""
    product = get_object_or_404(Product, id=product_id)
    testimonials = Testimonial.objects.filter(product_id=product_id).all()
    if request.method == 'POST':
        testimonial_obj = Testimonial.objects.filter(product_id=product_id).filter(user=request.user).get()
        new_testimonial = request.POST['edit_testimonial_text']
        testimonial_obj.testimonial_text = new_testimonial
        testimonial_obj.save()
        return redirect("product_detail", product_id)

    context = {"product": product,
               'testimonials': testimonials,
               'range': range(1, 6)}
    return render(request, 'products/edit_testimonial.html', context)


def edit_rating(request, product_id):
    """ Function to render the edit rating page"""
    product = get_object_or_404(Product, id=product_id)
    testimonials = Testimonial.objects.filter(product_id=product_id).all()

    if request.method == 'POST':
        user_rating = Decimal(request.POST['rate'])
        user_rate = UserRate(rating=user_rating,)
        Product.update_rating(product, user_rating)
        user_rate.save()
        return redirect("product_detail", product_id)

    context = {"product": product,
               'testimonials': testimonials,
               'range': range(1, 6)}
    return render(request, 'products/edit_rating.html', context)