from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders_history', views.orders_history, name='orders_history'),
    
]
