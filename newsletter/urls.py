from django.urls import path

from . import views

urlpatterns = [
    path('', views.subscribe_view, name='subscribe_view'),
]