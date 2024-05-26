from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userrate.models import UserRate
from testimonials.models import Testimonial
from cart import models
from django.shortcuts import get_object_or_404


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
        

        product_review = {}
        previous_product = "None"
        for product in products:
            if previous_product == product:
                break
            product = get_object_or_404(models.Product, pk=product.id)
            previous_product = product
            user_rate_exs = UserRate.objects.filter(user=request.user).filter(product_id=product.id).exists()
            testimonial_exs = Testimonial.objects.filter(user=request.user).filter(product_id=product.id).exists()
            if user_rate_exs:
                rate = UserRate.objects.filter(user=request.user).filter(product_id=product.id).get()
                product_review[product] = rate.rating
            if testimonial_exs:
                testimonial = Testimonial.objects.filter(user=request.user).filter(product_id=product.id).get()
                product_review[product] = testimonial.testimonial_text
            if user_rate_exs and testimonial_exs:
                testimonial = Testimonial.objects.filter(user=request.user).filter(product_id=product.id).get()
                rate = UserRate.objects.filter(user=request.user).filter(product_id=product.id).get()
                product_review[product] = [rate.rating, testimonial.testimonial_text]
            product_review[product] = []
        print(product_review)
        context = {'products': products,
                   'product_review': product_review,
                   'range': range(1, 6),
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
