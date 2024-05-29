from decimal import Decimal
from django.shortcuts import render
from cart.models import Product
from userrate.models import UserRate
from django.contrib import messages
from testimonials.models import Testimonial
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required
def testimonial(request, product_id):
    """ Function to handle users testimonials """

    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        user_rating = Decimal(request.POST['rate'])
        user_testimonial = request.POST['testimonial']
        user_rate_exs = UserRate.objects.filter(user=request.user).filter(product_id=product_id).exists()
        testimonial_exs = Testimonial.objects.filter(user=request.user).filter(product_id=product_id).exists()
        prevs_user_rate = UserRate.objects.filter(product_id=product_id).all()
    
        if not user_rate_exs:
            user_rate = UserRate(
                        user=request.user,
                        rating=user_rating,
                        product=product)
            user_rate.save()
            Product.update_rating(product, prevs_user_rate)

        if not testimonial_exs:
            inst_user_rate = UserRate.objects.filter(product_id=product_id).filter(user=request.user).get()
            testimonial_text = Testimonial(
                            user=request.user,
                            user_rating=inst_user_rate,
                            testimonial_text=user_testimonial,
                            product=product)
            testimonial_text.save()
        
        
        messages.info(request, "Your testimonial was submitted")
        return redirect("product_detail", product_id)

    messages.info(request, "Your testimonial was submitted")
    return redirect("product_detail", product_id)


@login_required
def edit_review(request, product_id):
    """ Function to render the edit testimonial"""
    product = get_object_or_404(Product, id=product_id)
    manage_review = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        user_rating = Decimal(request.POST['rate'])
        user_testimonial = request.POST['testimonial']
        user_rate = UserRate.objects.filter(user=request.user).filter(product_id=product_id).get()
        testimonial = Testimonial.objects.filter(user=request.user).filter(product_id=product_id).get()
        user_rate.rating = user_rating
        testimonial.testimonial_text = user_testimonial
        testimonial.save()
        user_rate.save()
        prevs_user_rate = UserRate.objects.filter(product_id=product_id).all()
        Product.update_rating(product, prevs_user_rate)
        messages.info(request, "You updated your review!")
        return redirect("product_detail", product_id)

    else:
        testimonial_exs = Testimonial.objects.filter(user=request.user).filter(product_id=product_id).exists()
        if testimonial_exs:
            testimonial_obj = Testimonial.objects.filter(product_id=product_id).filter(user=request.user).get()
        else:
            messages.warning(request, "You can only update your own reviews.")
            return redirect("product_detail", product_id)

    context = {"product": product,
               'manage_review': manage_review,
               "testimonial_obj": testimonial_obj,
               'range': range(1, 6)}


    context = {"product": product,
               'manage_review': manage_review,
               'range': range(1, 6)}

    return render(request, 'products/edit_review.html', context)


@login_required
def edit_testimonial(request, product_id):
    """ Function to render the edit testimonial"""
    product = get_object_or_404(Product, id=product_id)
    testimonials = Testimonial.objects.filter(product_id=product_id).all()

    if request.method == 'POST':
        testimonial_exs = Testimonial.objects.filter(user=request.user).filter(product_id=product_id).exists()
        if testimonial_exs:
            testimonial_obj = Testimonial.objects.filter(product_id=product_id).filter(user=request.user).get()
            new_testimonial = request.POST['edit_testimonial_text']
            testimonial_obj.testimonial_text = new_testimonial
            testimonial_obj.save()
            messages.info(request, "You edited your testimonial")
            return redirect("product_detail", product_id)

    context = {"product": product,
               'edit_review': edit_review,
               'testimonials': testimonials,
               'range': range(1, 6)}

    return render(request, 'products/edit_testimonial.html', context)

@login_required
def remove_testimonial(request, product_id):
    """ Function to render the edit rating page"""

    if 'obj' in request.GET:
        sort_method = request.GET['obj'].split('_')
        if 'testimonial' in sort_method:
            testimonial_obj = Testimonial.objects.filter(product_id=product_id).filter(user=request.user).exists()
            if testimonial_obj:
                testimonial_obj = Testimonial.objects.filter(product_id=product_id).filter(user=request.user).get()
                testimonial_obj.delete()
            else:
                pass

            rating_obj = UserRate.objects.filter(product_id=product_id).filter(user=request.user).exists()
            if rating_obj:
                rating_obj  = UserRate.objects.filter(product_id=product_id).filter(user=request.user).get()
                rating_obj.delete()
            else:
                pass

    messages.error(request, "You removed your testimonial")
    return redirect("product_review")
