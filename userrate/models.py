from django.db import models
from django.conf import settings
from products.models import Product


class UserRate(models.Model):
    """ User rate model """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="user_rate",
                             on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    product = models.ForeignKey(Product, related_name="rate_user_product",
                                on_delete=models.SET_NULL, null=True,
                                blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating}'