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
    order_total = 0
    delivery_cost = 0
    grand_total = 0
    items = []
    total_items = 0
    for items_id in cart:
        total_items += cart[items_id]['quantity']
        delivery_cost = 5 + 2*total_items
        unit_price = get_object_or_404(Product, id=items_id).price
        quantity[items_id] = cart[items_id]['quantity']
        order_total += unit_price * cart[items_id]['quantity']
        grand_total = delivery_cost + order_total
        items += Product.objects.filter(id=items_id).all()
        context = {'items': items, 'order_total': order_total, 
                   'delivery_cost': delivery_cost, 'grand_total': grand_total,
                   'cart': cart, 'total_items': total_items, 'quantity': quantity}
    return context
