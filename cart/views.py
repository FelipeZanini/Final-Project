import json
from . import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import stripe
from products.models import Product
from fezin import settings
from .forms import ShippingAddressForm
from .utils import cartData


def cart(request):
    context = cartData(request)
    return render(request, 'cart/cart.html', context)

def wishlist(request):
    context = {}
    try:
        wishlist = json.loads(request.COOKIES['wishlist'])
    except:
        wishlist = {}

    wishlistItems = []
    for items_id in wishlist:
        unit_price = get_object_or_404(Product, id=items_id).price
        wishlistItems += Product.objects.filter(id=items_id).all()
        context = {'wishlistItems': wishlistItems, 'unit_price': unit_price}
    return render(request, 'cart/wishlist.html', context)


@login_required
def checkout(request):
    context = cartData(request)
    form = ShippingAddressForm()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    context['form'] = form
    context['stripe_public_key'] = stripe_public_key
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            county = form.cleaned_data['county']
            eircode = form.cleaned_data['eircode']
            try:
                Order = models.Order(
                    user=request.user,
                        )
                ShippingAddress = models.ShippingAddress(
                        user=request.user,
                        order=Order,
                        address=address,
                        city=city,
                        county=county,
                        eircode=eircode,
                        )
            except:
                # Message
                return redirect('checkout')

            Order.save()
            ShippingAddress.save()

            for item in context['items']:
                try:
                    OrderItem = models.OrderItem(
                        product=item,
                        quantity=context['cart'][str(item.id)]['quantity'],
                        order=Order
                        )
                    OrderItem.save()
                except:
                    # Message
                    return redirect('checkout')

                OrderItem.save()       
    else:
        stripe_total = round(context['grand_total'] * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        context['client_secret'] = intent.client_secret
    return render(request, 'cart/checkout.html', context)
