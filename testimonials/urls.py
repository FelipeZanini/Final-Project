from django.urls import path
from . import views
urlpatterns = [
    path('testimonial/<int:product_id>/', views.testimonial,
         name='testimonial'),
    path('edit_testimonial/<int:product_id>/', views.edit_testimonial,
         name='edit_testimonial'),
    path('remove_testimonial/<int:product_id>/', views.remove_testimonial,
         name='remove_testimonial'),
]
