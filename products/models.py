from django.db import models
from django.conf import settings


class Category(models.Model):
    """ Category model """
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.friendly_name}'


class Product(models.Model):
    """ Product model """
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    def update_rating(self, prevs_user_rate):
        """ Update product rating function """
        avr = 0
        count = 0
        for value in prevs_user_rate:
            avr += int(value.rating)
            count += 1
        self.rating = avr/count
        self.save()

    def half_start(self):
        """ Function to check wheter would be a half start or full start """
        if self.rating - int(self.rating) >= 0.5:
            return True
        return False

    def __str__(self):
        return f'{self.name}'
