import json
import uuid
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
import stripe

from products.models import Product
from fezin import settings
from . import models
from .forms import ShippingAddressForm
from .utils import cart_data

@require_POST
def cache_checkout_data(request):
    """ View for cache checkout data  """
    try:
        data = cart_data(request)
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'data': json.dumps(data['cart']),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except TypeError:
        return HttpResponse(TypeError, status=400)


def cart(request):
    """ View to render cart template  """
    context = cart_data(request)
    return render(request, 'cart/cart.html', context)


def wishlist(request):
    """ View to render wishlist template  """
    context = {}
    try:
        wishlist_data = json.loads(request.COOKIES['wishlist'])
    except TypeError:
        wishlist_data = {}

    wishlist_items = []
    for items_id in wishlist_data:
        unit_price = get_object_or_404(Product, id=items_id).price
        wishlist_items += Product.objects.filter(id=items_id).all()
        context = {'wishlist_items': wishlist_items, 'unit_price': unit_price}
    return render(request, 'cart/wishlist.html', context)


@login_required
def checkout(request):
    """ View to render checkout template  """
    context = cart_data(request)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    form = ShippingAddressForm()
    context['form'] = form
    context['stripe_public_key'] = stripe_public_key

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            county = form.cleaned_data['county']
            eircode = form.cleaned_data['eircode']
            pid = request.POST.get('client_secret').split('_secret')[0]

            try:
                order = models.Order(
                    user=request.user,
                    email=request.user.email,
                    order_number=uuid.uuid4().hex.upper(),
                    complete=True,
                    delivery_cost=context['delivery_cost'],
                    order_total=context['order_total'],
                    grand_total=context['grand_total'],
                    stripe_pid=pid,
                        )

                shipping_address = models.ShippingAddress(
                        user=request.user,
                        order=order,
                        address=address,
                        city=city,
                        county=county,
                        eircode=eircode,
                        )
                order.save()
                shipping_address.save()

                for item in context['items']:
                    order_item = models.OrderItem(
                        user=request.user,
                        product=item,
                        quantity=context['cart'][str(item.id)]['quantity'],
                        order=order
                        )
                    order_item.save()

            except TypeError:
                return redirect('checkout')

            return redirect(
                reverse('checkout_success', args=[order.order_number]))

    else:
        stripe_total = round(100*context['grand_total'])
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        context['client_secret'] = intent.client_secret

    return render(request, 'cart/checkout.html', context)


@login_required
def checkout_success(request, order_number):
    """ View to render checkout success template  """
    order = get_object_or_404(models.Order, order_number=order_number)
    shipping_address = get_object_or_404(models.ShippingAddress,
                                         order__order_number=order_number)
    order_item = models.OrderItem.objects.filter(order=order).all()
    order_total = False


    send_mail(
        f"Order: {order_number.order_number}",
        f"Thank you for your purchase, we are glad to have you shopping with us. Grand Total:{order.grant_total} $,{order.date_ordered}",
        settings.DEFAULT_FROM_EMAIL,
        [request.user.email]
        )

    

    context = {'order': order, 'shipping_address': shipping_address,
               'order_item': order_item, 'order_total': order_total} 

    return render(request, 'cart/checkout_success.html', context)
