from django.urls import path
from .views import index, catalog

urlpatterns = [
    path('', index),
    path('catalog', catalog)
]