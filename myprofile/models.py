from django.db import models
from django.conf import settings


class AddressProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="order_user_profile",
                             on_delete=models.SET_NULL, null=True, blank=True)
    address_line = models.CharField(max_length=254, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    eircode = models.CharField(max_length=254, null=False, blank=False)
    county = models.CharField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=254, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
