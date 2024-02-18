from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)


admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Order, OrderAdmin)
