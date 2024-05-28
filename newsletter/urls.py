from django.urls import path

from . import views

urlpatterns = [
    path('', views.subscribe_view, name='subscribe_view'),
    path('subscribe_success_view/', views.subscribe_success_view, name='subscribe_success_view'),
    path('subscribe_fail_view/', views.subscribe_fail_view, name='subscribe_fail_view'),
    path('unsubscribe_view/', views.unsubscribe_view, name='unsubscribe_view'),
    path('unsubscribe_success_view/', views.unsubscribe_success_view, name='unsubscribe_success_view'),
    path('unsubscribe_fail_view/', views.unsubscribe_fail_view, name='unsubscribe-fail'),
]