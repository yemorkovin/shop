from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('panel', panel),
    path('reg_post', reg_post),
    path('auth_post', auth_post),
    path('logout', logout),
    path('addcart', addcart),
    path('cart', cart)
]