from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userrate.models import UserRate
from testimonials.models import Testimonial
from django.contrib import messages
from cart import models
from .models import AddressProfile
from django.shortcuts import get_object_or_404


@login_required
def profile(request):
    """ Function to render the profile page """
    context = {}
    try:
        user_address = []
        products = models.OrderItem.objects.filter(user=request.user).all()
        unique_products = []
        for product in products:
            if product.product.name not in unique_products:
                unique_products.append(product.product.name)
        user_address_exists = AddressProfile.objects.filter(user=request.user).exists()
        if request.method == 'POST':
            user_address_exists = AddressProfile.objects.filter(user=request.user).exists()
            if not user_address_exists:
                address_line = request.POST['address-profile']
                city = request.POST['city-address-profile']
                eircode = request.POST['eircode-profile']
                county = request.POST['county-profile']
                phone = request.POST['phone-profile']
            
                address = AddressProfile(
                user = request.user,
                address_line=address_line,
                city=city,
                eircode=eircode,
                county =county,
                phone=phone,)
                address.save()
                user_address = AddressProfile.objects.filter(user=request.user).get()
                messages.info(request, "Your address was successfully submitted")
            else:
                address_line = request.POST['address-profile']
                city = request.POST['city-address-profile']
                eircode = request.POST['eircode-profile']
                county = request.POST['county-profile']
                phone = request.POST['phone-profile']
                
                update_address = get_object_or_404(AddressProfile, user=request.user)
                update_address.user = request.user
                update_address.address_line=address_line
                update_address.city=city
                update_address.eircode=eircode
                update_address.county =county
                update_address.phone=phone
                update_address.save()
                
                messages.info(request, "Your address was successfully updated")
                
        if user_address_exists:
            user_address = AddressProfile.objects.filter(user=request.user).get()

        
        context = {'user_address': user_address,
                    'products': unique_products}

    
    except TypeError:
        messages.info(request, "Sorry, a error has occured!")
    
    return render(request, 'profile/profile.html', context)

@login_required
def delete_profile_address(request):
    """ Function to delete profile address """
    context = {}
    try:
        address = get_object_or_404(AddressProfile, user=request.user)
        address.delete()
        messages.info(request, "Your address was successfully deleted")

    except TypeError:
        messages.info(request, "Sorry, a error has occured!")

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
            product = get_object_or_404(models.Product, pk=product.product_id)
            product_review[product] = []
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
