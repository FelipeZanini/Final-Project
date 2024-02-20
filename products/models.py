from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    def update_rating(self, prevs_user_rate):
        avr = 0
        count = 0
        for value in prevs_user_rate:
            avr += int(value.rating)
            
        self.rating = (avr/count)
        self.save()

    def half_start(self):
        if self.rating - int(self.rating) >= 0.5:
            return True

    def __str__(self):
        return self.name


class UserRate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="user_rate",
                             on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product = models.ForeignKey(Product, related_name="rate_user_product", on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating}'


class Testimonial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="user_testimonial",
                             on_delete=models.SET_NULL, null=True, blank=True)
    testimonial_text = models.TextField(max_length=100, null=True, blank=True)
    user_rating = models.ForeignKey(UserRate, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, related_name="testimonial_user_product", on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.user} {self.product} {self.date_added}'
