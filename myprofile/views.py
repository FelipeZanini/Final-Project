from django.shortcuts import render, get_object_or_404
from cart import models


def profile(request):
    context = {}
    unique_email = request.user.email
    try:
        orders = models.Order.objects.filter(email=unique_email).all()
        context = {'orders': orders}
    except TypeError:
        print("No orders")
    return render(request, 'profile/profile.html', context)
