from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.products, name='products'),
    path('product_detail/<int:product_id>/', views.product_detail,
        name='product_detail'),
    path('testimonial/<int:product_id>/', views.testimonial, name='testimonial'),
    path('edit_testimonial/<int:product_id>/', views.edit_testimonial, name='edit_testimonial'),
    path('edit_rating/<int:product_id>/', views.edit_rating, name='edit_rating'),
    path('remove_review/<int:product_id>/', views.remove_review, name='remove_review'),
]
