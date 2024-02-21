from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup'),
]
