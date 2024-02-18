import json
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_data(request):
    bag_data = {}
    try:
        cart = json.loads(request.COOKIES['cart'])
    except TypeError:
        print(TypeError)
        cart = {}

    items = []
    quantity = {}
    order_total = 0
    delivery_cost = 0
    grand_total = 0
    total_items = 0
    for items_id in cart:
        items += Product.objects.filter(id=items_id).all()
        unit_price = get_object_or_404(Product, id=items_id).price
        order_total += unit_price * cart[items_id]['quantity']
        delivery_cost = 5 + 2*total_items
        grand_total = delivery_cost + order_total
        total_items += cart[items_id]['quantity']
        quantity[items_id] = cart[items_id]['quantity']

        bag_data = {'delivery_cost': delivery_cost, 'quantity': quantity,
                    'items': items, 'order_total': order_total, 'cart': cart,
                    'grand_total': grand_total, 'total_items': total_items}
    return bag_data
