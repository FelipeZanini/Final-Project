from django.contrib import admin
from .models import Product, Category, UserRate, Testimonial

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(UserRate)
admin.site.register(Testimonial)
