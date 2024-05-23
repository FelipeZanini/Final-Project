from django.urls import path

from . import views

urlpatterns = [
    path('ping/', views.mailchimp_ping_view),
    path('', views.subscribe_view, name='subscribe'),
    path('subscribe_success_view/', views.subscribe_success_view, name='subscribe_success_view'),
    path('subscribe_fail_view/', views.subscribe_fail_view, name='subscribe_fail_view'),
    path('unsubscribe/', views.unsubscribe_view, name='unsubscribe'),
    path('unsubscribe_success_view/', views.unsubscribe_success_view, name='unsubscribe_success_view'),
    path('unsubscribe_fail_view/', views.unsubscribe_fail_view, name='unsubscribe-fail'),
]