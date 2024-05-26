from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    path('product_review', views.product_review, name='product_review'),
    path('delete_profile_address', views.delete_profile_address, name='delete_profile_address'),
    path('orders_history', views.orders_history, name='orders_history'),
]
