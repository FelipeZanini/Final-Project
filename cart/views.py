from django.shortcuts import render, get_object_or_404
import json
from .models import * 
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

    items = []
    for items_id in wishlist:
        unit_price = get_object_or_404(Product, id=items_id).price
        items += Product.objects.filter(id=items_id).all()
        context = {'items': items, 'unit_price': unit_price}
    return render(request, 'cart/wishlist.html', context)

