from django.urls import path
from . import views
urlpatterns = [
    path('edit_rating/<int:product_id>/', views.edit_rating,
         name='edit_rating')
]
