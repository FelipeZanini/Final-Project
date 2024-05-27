from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('profile/', include('myprofile.urls')),
    path('edit_rating/', include('userrate.urls')),
    path('edit_review/', include('testimonials.urls')),
    path('contact_us/', include('contactus.urls')),
]

handler404 = 'home.views.error_404'
