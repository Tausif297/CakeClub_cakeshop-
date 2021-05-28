from django.urls import path
from . import views

urlpatterns = [
    path('cakes/',views.cake,name='cakeproductpage'),
    path('cakes/checkout/', views.checkout, name='checkoutpage'),
]
