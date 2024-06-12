from django.urls import path

from . import views

urlpatterns = [
    path('newsletter_subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]