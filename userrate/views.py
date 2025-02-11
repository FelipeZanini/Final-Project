from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from testimonials.models import Testimonial
from userrate.models import UserRate
from cart.models import Product



@login_required
def edit_rating(request, product_id):
    """ Function to render the edit rating page"""
    product = get_object_or_404(Product, id=product_id)
    prevs_user_rate = UserRate.objects.filter(product_id=product_id).all()

    if request.method == 'POST':
        user_rate = UserRate.objects.filter(product_id=product_id).filter(user=request.user).get()
        user_rating = Decimal(request.POST['rate'])
        user_rate.rating = user_rating
        user_rate.save()
        Product.update_rating(product, prevs_user_rate)
        messages.info(request, "You edited your rating")
        return redirect("product_detail", product_id)
    
    try:
        testimonial_obj = Testimonial.objects.filter(product_id=product_id).filter(user=request.user).get()
        context = {"product": product,
                   "testimonial_obj": testimonial_obj,
                   }
        return render(request, 'products/edit_rating.html', context)
    except:
        messages.warning(request, "You can only update your own rating.")
        return redirect("product_detail", product_id)


    context = {"product": product}

    return render(request, 'products/edit_rating.html', context)