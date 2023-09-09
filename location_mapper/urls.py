# location_mapper/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.location_list, name='location_list'),
    path('<str:custom_name>/', views.location_detail, name='location_detail'),  # Use custom_name in the URL
    path('location/add_location/', views.add_location, name='add_location'),  # New URL pattern for adding locations
]
