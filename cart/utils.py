import json
from .models import *
from products.models import Product
from django.shortcuts import get_object_or_404

def cartData(request):
    context = {}
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    quantity = {}
    grand_total = 0
    items = []
    total_items = 0
    for items_id in cart:
        total_items += cart[items_id]['quantity']
        unit_price = get_object_or_404(Product, id=items_id).price
        quantity[items_id] = cart[items_id]['quantity']
        grand_total += unit_price * cart[items_id]['quantity']
        items += Product.objects.filter(id=items_id).all()
        context = {'items': items, 'grand_total': grand_total, 'cart': cart, 'total_items': total_items, 'quantity': quantity}
    return context
