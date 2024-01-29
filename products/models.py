from django.db import models


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
    image =  models.CharField(max_length=255, null=True, blank=True)
    size = models.BooleanField(default=False, null=True, blank=True)
    def half_start(self):
        if self.rating -int(self.rating) >= 0.5:
            return True

    def __str__(self):
        return self.name