from django import forms
from .models import ShippingAddress


class  ShippingAddressForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'county', 'eircode']

    address = forms.CharField(max_length=100, label='Address')
    city = forms.CharField(max_length=50, label='City')
    county = forms.CharField(max_length=50, label='County')
    eircode = forms.CharField(max_length=7, label='Eircode')