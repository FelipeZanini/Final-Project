from django.urls import path
from . import views
urlpatterns = [
    path('testimonial/<int:product_id>/', views.testimonial,
         name='testimonial'),
    path('edit_testimonial/<int:product_id>/', views.edit_testimonial,
         name='edit_testimonial'),
         path('edit_review/<int:product_id>/', views.edit_review,
         name='edit_review'),
    path('remove_testimonial/<int:product_id>/', views.remove_testimonial,
         name='remove_testimonial'),
]
