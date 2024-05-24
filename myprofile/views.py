from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userrate.models import UserRate
from testimonials.models import Testimonial
from cart import models


@login_required
def profile(request):
    """ Function to render the profile page """
    context = {}
    try:
        products = models.OrderItem.objects.filter(user=request.user).all()
        context = {'products': products}
        testimonials = Testimonial.objects.filter(user=request.user).all()
        user_rates = UserRate.objects.filter(user=request.user).all()

        context = {'products': products,
                   'testimonials': testimonials,
                   'user_rates': user_rates}

    except TypeError:
        print("No products")

    return render(request, 'profile/profile.html', context)


@login_required
def product_review(request):
    """ Function to render the products order """
    context = {}
    try:
        products = models.OrderItem.objects.filter(user=request.user).all()
        context = {'products': products}
        testimonials = Testimonial.objects.filter(user=request.user).all()
        user_rates = UserRate.objects.filter(user=request.user).all()

        context = {'products': products,
                   'testimonials': testimonials,
                   'user_rates': user_rates}

    except TypeError:
        print("No products")

    return render(request, 'profile/product_review.html', context)


@login_required
def orders_history(request):
    """ Function to render the orders history page """
    context = {}
    unique_email = request.user.email
    try:
        orders = models.Order.objects.filter(email=unique_email).all()
        context = {'orders': orders}
    except TypeError:
        print("No orders")

    return render(request, 'profile/orders_history.html', context)
