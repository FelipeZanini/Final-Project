from django.db import models
from django.conf import settings
from products.models import Product
from userrate.models import UserRate


class Testimonial(models.Model):
    """ Testimonial model """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="user_testimonial",
                             on_delete=models.SET_NULL, null=True, blank=True)
    testimonial_text = models.TextField(max_length=100, null=True, blank=True)
    user_rating = models.ForeignKey(UserRate, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    product = models.ForeignKey(
        Product, related_name="testimonial_user_product",
        on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.user} {self.product} {self.date_added}'
