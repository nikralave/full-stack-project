from django.urls import path,include
from .views import view_cart, add_to_cart, remove_from_cart, adjust_cart


urlpatterns = [
     path('', view_cart, name= 'view_cart'),
     path('add', add_to_cart, name= 'add_to_cart'),
     path('remove(<id>\d+)', remove_from_cart, name='remove_from_cart'),
      path('adjust(<id>\d+)', adjust_cart, name='adjust_cart'),
    
    ]